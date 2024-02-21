from scapy.fields import LEIntField, LEIntEnumField
from scapy.packet import Packet

from .. import enums


class LoadTube(Packet):
    name = "Load Tube "
    fields_desc = [
        LEIntField("tube_index", 0),
        LEIntEnumField("ordnance_type", 0, enums.ordnance_type),
        LEIntField("unknown1", 0),
        LEIntField("unknown2", 0),
    ]
