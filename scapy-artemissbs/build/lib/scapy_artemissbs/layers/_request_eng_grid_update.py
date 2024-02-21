from scapy.fields import LEIntField
from scapy.packet import Packet


class RequestEngGridUpdate(Packet):
    name = "RequestEngGridUpdate "
    fields_desc = [
        LEIntField("unknown", 0),
    ]
