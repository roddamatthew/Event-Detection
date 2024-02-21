import struct

from scapy.fields import Field


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
