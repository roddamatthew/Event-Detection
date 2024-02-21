from scapy.packet import Packet

from ..fields import ArtemisSBSFloatField


class SimpleEvent08(Packet):
    name = "Simple Event 08"
    fields_desc = [
        ArtemisSBSFloatField("unknown", 0),
    ]
