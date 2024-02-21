from scapy.fields import LEIntEnumField
from scapy.packet import Packet

from .. import enums
from ..fields import ArtemisSBSFloatField


class EngSetEnergy(Packet):
    name = "Engineering Set Energy "
    fields_desc = [
        ArtemisSBSFloatField("value", 0.5),
        LEIntEnumField("ship_system", 0, enums.ship_system),
    ]
