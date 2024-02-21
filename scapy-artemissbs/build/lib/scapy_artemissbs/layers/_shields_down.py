from scapy.fields import LEIntField
from scapy.packet import Packet


class ShieldsDown(Packet):
    name = "Shields Down "
    fields_desc = [LEIntField("unused", 0)]
