from scapy.fields import XLEIntField
from scapy.packet import Packet


class Ready(Packet):
    name = "Ready "
    fields_desc = [
        XLEIntField("unknown", 0),
    ]
