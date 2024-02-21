from scapy.fields import LEIntField, LEIntEnumField
from scapy.packet import Packet

from .. import enums


class EngSetCoolant(Packet):
    name = "Engineering Set Coolant "
    fields_desc = [
        LEIntEnumField("ship_system", 0, enums.ship_system),
        LEIntField("value", 0),
        LEIntField("unknown1", 0),
        LEIntField("unknown2", 0),
    ]
