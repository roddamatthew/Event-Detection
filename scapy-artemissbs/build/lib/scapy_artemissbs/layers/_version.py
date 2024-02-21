import struct

from scapy.fields import Field, XLEIntField
from scapy.packet import Packet

from ..fields import ArtemisSBSFloatField


class VersionField(Field):
    def getfield(self, pkt, s):
        return s[12:], ".".join(map(str, struct.unpack("<III", s[:12])))

    def addfield(self, pkt, s, val):
        return s + struct.pack("<III", *tuple(map(int, val.split("."))))


class Version(Packet):
    name = "Welcome "
    fields_desc = [
        XLEIntField("unknown", 0),
        ArtemisSBSFloatField("version_deprecated", 0),
        VersionField("version", "0.0.0"),
    ]
