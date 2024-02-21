from scapy.packet import Packet

from ..fields import ArtemisSBSFloatField


class HelmJump(Packet):
    name = "Helm Jump "
    fields_desc = [
        ArtemisSBSFloatField("bearing", 0),
        ArtemisSBSFloatField("distance", 0),
    ]
