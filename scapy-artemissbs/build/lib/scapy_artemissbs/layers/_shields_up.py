from scapy.fields import LEIntField
from scapy.packet import Packet


class ShieldsUp(Packet):
    name = "Shields Up "
    fields_desc = [LEIntField("unused", 0)]
