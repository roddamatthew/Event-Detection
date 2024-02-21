from scapy.fields import LEIntField
from scapy.packet import Packet


class FireTube(Packet):
    name = "Fire Tube "
    fields_desc = [LEIntField("tube_index", 0)]
