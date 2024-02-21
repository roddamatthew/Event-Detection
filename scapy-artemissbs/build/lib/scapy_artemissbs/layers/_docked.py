from scapy.fields import LEIntField
from scapy.packet import Packet


class Docked(Packet):
    name = "Docked "
    fields_desc = [LEIntField("object_id", 0)]
