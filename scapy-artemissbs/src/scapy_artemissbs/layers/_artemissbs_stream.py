import struct

from scapy.fields import PacketListField
from scapy.packet import Packet

from ._artemissbs import ArtemisSBS


class ArtemisSBSStream(Packet):
    name = "Artemis Spaceship Bridge Simulator Stream"
    fields_desc = [
        PacketListField(
            "packets",
            [],
            ArtemisSBS,
        )
    ]

    @classmethod
    def tcp_reassemble(cls, data, metadata):
        length = metadata.get("length", 0)
        while length < len(data):
            length = length + struct.unpack("<I", data[length + 4 : length + 8])[0]
        if length == len(data):
            return cls(data)
        metadata["length"] = length
        return None
