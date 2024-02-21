from scapy.fields import LEIntField
from scapy.packet import Packet


class SimpleEvent19(Packet):
    name = "Simple Event 19"
    fields_desc = [
        LEIntField("unknown", 0),
    ]
