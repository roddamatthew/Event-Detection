from scapy.fields import LEIntField
from scapy.packet import Packet

from ..fields import ArtemisSBSFloatField


class Smoke(Packet):
    name = "Smoke "
    fields_desc = [
        LEIntField("object_id", 0),
        LEIntField("priority", 0),
        ArtemisSBSFloatField("x", 0),
        ArtemisSBSFloatField("y", 0),
        ArtemisSBSFloatField("z", 0),
    ]
