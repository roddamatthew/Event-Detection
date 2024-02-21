from typing import Tuple, Optional

from scapy.fields import LEIntEnumField, LEIntField, _FieldContainer
from scapy.packet import Packet

from .. import enums
from ..fields import ArtemisSBSFloatField, ArtemisSBSBooleanField, ArtemisSBSStrField


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


class ShipSettings(Packet):
    fields_desc = [
        LEIntEnumField("drive_type", 0, enums.drive_type),
        LEIntField("hull_id", 0),
        ArtemisSBSFloatField("accent_color", 0),
        FlaggedField(
            ArtemisSBSBooleanField("has_name", False), ArtemisSBSStrField("name", None)
        ),
    ]

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
