import struct

from scapy.fields import Field
from scapy.packet import Packet

from ..fields import ArtemisSBSStrField


class CustomStrField(Field):
    def getfield(self, pkt, s):
        s, length = s[4:], struct.unpack("<I", s[:4])[0]
        return s[length + 1 :], s[:length].decode("ascii")

    def addfield(self, pkt, s, val):
        s += struct.pack(">I", len(val))
        s += val.encode("ascii") + b"\x00"
        return s


class Welcome(Packet):
    name = "Welcome "
    fields_desc = [
        ArtemisSBSStrField("welcome_message", 0),
    ]
