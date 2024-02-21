import math
import struct
from typing import Any, List, Optional, Tuple, TypeVar, Union

from scapy.fields import (
    ByteField,
    ConditionalField,
    Field,
    FlagsField,
    FlagValue,
    LEIntField,
    LEShortField,
    _FieldContainer,
)
from scapy.packet import Packet


class CustomStrField(Field):
    def getfield(self, pkt, s):
        s, length = s[4:], struct.unpack("<I", s[:4])[0]
        return s[length + 1 :], s[:length].decode("ascii")

    def addfield(self, pkt, s, val):
        s += struct.pack(">I", len(val))
        s += val.encode("ascii") + b"\x00"
        return s


class XLEVarIntField(Field):
    __slots__ = ["length_from"]

    def __init__(self, name, default, length_from):
        super().__init__(name, default)
        self.length_from = length_from

    def getfield(self, pkt, s):
        length = self.length_from(pkt)
        return s[length:], int.from_bytes(s[:length], "little")

    def addfield(self, pkt, s, val):
        length = self.length_from(pkt)
        return s + val.to_bytes(length, byteorder="little")

    def i2repr(self, pkt, x):
        return hex(x)


class ConstantField(Field):
    __slots__ = ["_field"]

    def __init__(self, field):
        super().__init__(field.name, field.default)
        self._field = field

    def getfield(self, pkt, s):
        s, val = self._field.getfield(pkt, s)
        if val != self.default:
            raise ValueError(
                f"Field {self.name} is not expected value {self.default}, but {val}"
            )
        return s, val

    def addfield(self, pkt, s, val):
        return self._field.addfield(pkt, s, val)

    def i2repr(self, pkt, x):
        return self._field.i2repr(pkt, x)


class FlaggedField(_FieldContainer):
    __slots__ = ["cond_fld", "fld"]

    def __init__(self, cond_fld, fld):
        self.cond_fld = cond_fld
        self.fld = fld

    def getfield(self, pkt, s):
        s, present = self.cond_fld.getfield(pkt, s)
        if present:
            s, val = self.fld.getfield(pkt, s)
        else:
            val = None
        return s, val

    def addfield(self, pkt, s, val):
        if val is not None:
            s = self.cond_fld.addfield(pkt, s, True)
            s = self.fld.addfield(pkt, s, val)
        else:
            s = self.cond_fld.addfield(pkt, s, False)
        return s


class MetaField(Field):
    __slots__ = ["val_from"]

    def __init__(self, name, default, val_from):
        super().__init__(name, default)
        self.val_from = val_from

    def getfield(self, pkt, s):
        s, val = s, self.val_from(pkt)
        return s, val

    def addfield(self, pkt, s, val):
        return s

    def i2h(self, pkt, x):
        return self.val_from(pkt)

    def i2repr(self, pkt, x):
        return self.val_from(pkt)


class VersionField(Field):
    def getfield(self, pkt, s):
        return s[12:], ".".join(map(str, struct.unpack("<III", s[:12])))

    def addfield(self, pkt, s, val):
        return s + struct.pack("<III", *tuple(map(int, val.split("."))))


class SystemGridStatusField(Field):
    def getfield(self, pkt, s):
        grid_statuses = []
        while not s.startswith(b"\xff"):
            s, (x, y, z, damage) = s[7:], struct.unpack("<BBBf", s[:7])
            grid_statuses.append({"x": x, "y": y, "z": z, "damage": damage})
        s = s[1:]

        return s, grid_statuses

    def addfield(self, pkt, s, val):
        for status in val:
            s += struct.pack(
                "<BBBf", status["x"], status["y"], status["z"], status["damage"]
            )
        return s + b"\xff"


class DAMCONTeamStatusField(Field):
    def getfield(self, pkt, s):
        team_statuses = []

        while not s.startswith(b"\xfe"):
            s, values = s[33:], struct.unpack("<BIIIIIIfI", s[:33])
            team_statuses.append(
                dict(
                    zip(
                        [
                            "team_id",
                            "goal_x",
                            "current_x",
                            "goal_y",
                            "current_y",
                            "goal_z",
                            "current_z",
                            "progress",
                            "number_of_team_members",
                        ],
                        values,
                    )
                )
            )

        s = s[1:]

        return s, team_statuses

    def addfield(self, pkt, s, val):
        for status in val:
            s += struct.pack(
                "<BIIIIIIfI",
                *[
                    status[key]
                    for key in [
                        "team_id",
                        "goal_x",
                        "current_x",
                        "goal_y",
                        "current_y",
                        "goal_z",
                        "current_z",
                        "progress",
                        "number_of_team_members",
                    ]
                ],
            )
        return s + b"\xfe"


class ArtemisSBSBooleanField(Field):
    __slots__ = ["_field"]

    def __init__(self, name, default):
        super().__init__(name, default)
        self._field = LEIntField(name, 0)

    def getfield(self, pkt, s):
        s, flag = self._field.getfield(pkt, s)
        return s, bool(flag)

    def addfield(self, pkt, s, val):
        return self._field.addfield(pkt, s, int(val))


class ArtemisSBSByteBooleanField(Field):
    __slots__ = ["_field"]

    def __init__(self, name, default):
        super().__init__(name, default)
        self._field = ByteField(name, 0)

    def getfield(self, pkt, s):
        s, flag = self._field.getfield(pkt, s)
        return s, bool(flag)

    def addfield(self, pkt, s, val):
        return self._field.addfield(pkt, s, int(val))


def ljust_list(list_: List, length, fill_value):
    return list_ + (length - len(list_)) * [fill_value]


class ArtemisSBSFlagsField(FlagsField):
    def __init__(
        self,
        name: str,
        default: Optional[Union[int, FlagValue]],
        names: List[str],
        fill_prefix="unused",
    ) -> None:
        size = len(names)
        n_bytes = (size // 8 + 1) if (size % 8 == 0) else int(math.ceil(size / 8))
        padding = n_bytes * 8 - size

        reordered_names: List[str] = []
        for i in range(n_bytes):
            reordered_names = (
                ljust_list(names[8 * i : 8 * (i + 1)], 8, fill_prefix) + reordered_names
            )

        super().__init__(name, default, size + padding, reordered_names)


class ArtemisSBSFloatField(Field[int, int]):
    def __init__(self, name, default):
        Field.__init__(
            self, name, default, "<f"
        )  # There was some problem using super() here, haven't been able to work out why.


class ArtemisSBSShortBooleanField(Field):
    __slots__ = ["_field"]

    def __init__(self, name, default):
        super().__init__(name, default)
        self._field = LEShortField(name, 0)

    def getfield(self, pkt, s):
        s, flag = self._field.getfield(pkt, s)
        return s, bool(flag)

    def addfield(self, pkt, s, val):
        return self._field.addfield(pkt, s, int(val))


class ArtemisSBSStrField(Field):
    __slots__ = ["length_struct"]

    def __init__(self, name, default):
        super().__init__(name, default)
        self.length_struct = struct.Struct("<I")

    # def i2m(self, pkt, x):
    #     return self.length_struct.pack(len(x) + 1) + x.encode("utf-16le") + b"\x00\x00"

    def getfield(self, pkt, s):
        s, length = s[4:], self.length_struct.unpack(s[:4])[0]
        s, val = s[length * 2 :], s[: length * 2 - 2].decode("utf-16le")
        return s, val

    def addfield(self, pkt, s, val):
        length = len(val) + 1
        s += self.length_struct.pack(length)
        s += val.encode("utf-16le") + b"\x00\x00"
        return s


class PropertyField(ConditionalField):
    def __init__(self, fld: Field[Any, Any]) -> None:
        super().__init__(fld, lambda pkt: pkt.flags and fld.name in pkt.flags)

    def addfield(self, pkt: Packet, s: bytes, val: Any) -> bytes:
        return s if val is None else self.fld.addfield(pkt, s, val)

    def i2h(self, pkt: Optional[Packet], val: Any):
        return self.fld.i2h(pkt, val)


I = TypeVar("I")


class PropertyFlagsField(ArtemisSBSFlagsField):
    def addfield(
        self, pkt: Packet, s: Union[Tuple[bytes, int, int], bytes], ival: I
    ) -> Union[Tuple[bytes, int, int], bytes]:
        if ival is None:
            ival = self.any2i(
                pkt,
                [attr for attr in self.names if getattr(pkt, attr, None) is not None],
            )
        return super().addfield(pkt, s, ival)
