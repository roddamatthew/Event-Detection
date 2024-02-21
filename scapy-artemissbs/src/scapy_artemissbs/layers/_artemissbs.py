import struct
from typing import Optional, Tuple, Any

from scapy.packet import Packet
from scapy.fields import (
    LEIntEnumField,
    LEIntField,
    Field,
    XLEIntField,
    _FieldContainer,
    ActionField,
)

from .. import enums


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


# class TypeField(Field):
#     def getfield(self, pkt, s):
#         s, type_ = s[4:], struct.unpack("<I", s[:4])[0]
#         subtype_length = self._subtype_len(type_)
#         s, subtype = s[subtype_length:], int.from_bytes(s[:subtype_length], "little")
#         val = (type_, subtype)
#         return s, val

#     def addfield(self, pkt, s, val):
#         type_, subtype = val
#         subtype_length = self._subtype_len(type_)
#         s += struct.pack("<I", type_)
#         s += subtype.to_bytes(subtype_length, byteorder="little")
#         return s

#     def i2repr(self, pkt, x):
#         return enums.packet_types[x]

#     @classmethod
#     def _subtype_len(cls, type_):
#         return {
#             0x0351A5AC: 4,
#             0x4C821D3C: 4,
#             0x69CC01D9: 4,
#             0x26FAACB9: 1,
#             0xF754C8FE: 4,
#         }.get(type_, 0)

#     @classmethod
#     def calc_len(cls, pkt):
#         return 4 + cls._subtype_len(pkt.type[0])


# class SubtypeField(Field):
#     def getfield(self, pkt, s):
#         subtype_length = self.subtype_len(pkt)
#         s, val = s[subtype_length:], int.from_bytes(s[:subtype_length], "little")
#         return s, val

#     def addfield(self, pkt, s, val):
#         subtype_length = self.subtype_len(pkt)
#         s += val.to_bytes(subtype_length, byteorder="little")
#         return s

#     @classmethod
#     def subtype_len(cls, pkt):
#         return {
#             0x0351A5AC: 4,
#             0x4C821D3C: 4,
#             0x69CC01D9: 4,
#             0x26FAACB9: 1,
#             0xF754C8FE: 4,
#         }.get(pkt.type, 0)


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


subtype_lengths = {
    0x0351A5AC: 4,
    0x4C821D3C: 4,
    0x69CC01D9: 4,
    0x26FAACB9: 1,
    0xF754C8FE: 4,
}


class ArtemisSBS(Packet):
    name = "Artemis Spaceship Bridge Simulator "
    fields_desc = [
        ConstantField(XLEIntField("header", 0xDEADBEEF)),
        LEIntField("len", None),
        LEIntEnumField("origin", 1, {1: "server", 2: "client"}),
        ConstantField(LEIntField("padding", 0)),
        LEIntField("remaining", None),
        LEIntEnumField(
            "internal_type",
            0x80803DF9,
            enums.internal_type,
        ),
        XLEVarIntField(
            "internal_subtype",
            0,
            lambda pkt: subtype_lengths.get(pkt.internal_type, 0),
        ),
        MetaField(
            "type",
            "",
            lambda pkt: enums.packet_type[
                (pkt.origin, pkt.internal_type, pkt.internal_subtype)
            ],
        ),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = None

    def post_build(self, p, pay):
        if self.len is None:
            p = p[:4] + struct.pack("<I", len(p + pay)) + p[8:]
        if self.remaining is None:
            p = p[:16] + struct.pack("<I", len(p + pay) - 20) + p[20:]
        return p + pay

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        payload_len = self.len - (24 + subtype_lengths.get(self.internal_type, 0))
        payload, padding = s[:payload_len], s[payload_len:]
        return payload, padding

    def _update_type(self, val, fld):
        flds = ["origin", "internal_type", "internal_subtype"]
        key = tuple(val if f == fld.name else getattr(self, fld) for f in flds)
        self.type = enums.packet_type(key)
