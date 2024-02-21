from scapy.packet import Packet

from ..fields import ArtemisSBSFloatField


class CloakDecloak(Packet):
    name = "Cloak/Decloak "
    fields_desc = [
        ArtemisSBSFloatField("x", 0),
        ArtemisSBSFloatField("y", 0),
        ArtemisSBSFloatField("z", 0),
    ]
