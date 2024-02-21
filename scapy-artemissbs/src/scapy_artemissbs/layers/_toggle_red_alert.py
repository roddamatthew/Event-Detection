from scapy.fields import XLEIntField
from scapy.packet import Packet


class ToggleRedAlert(Packet):
    name = "Toggle Red Alert "
    fields_desc = [XLEIntField("unused", 0)]
