from scapy.fields import LEIntField
from scapy.packet import Packet


class HelmToggleReverse(Packet):
    name = "Helm Toggle Reverse "
    fields_desc = [LEIntField("unused", 0)]
