from scapy.fields import LEIntEnumField, LEIntField
from scapy.packet import Packet

from .. import enums


class Detonation(Packet):
    name = "Detonation "
    fields_desc = [
        LEIntEnumField("object_type", 0, enums.object_type),
        LEIntField("object_id", 0),
    ]
