from scapy.packet import Packet

from ..fields import ArtemisSBSFloatField


class GameMasterSelectLocation(Packet):
    name = "Game Master Select Location "
    fields_desc = [
        ArtemisSBSFloatField("z", 0),
        ArtemisSBSFloatField("y", 0),
        ArtemisSBSFloatField("x", 0),
    ]
