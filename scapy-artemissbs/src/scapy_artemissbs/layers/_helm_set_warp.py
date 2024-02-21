from scapy.fields import LEIntField
from scapy.packet import Packet


class HelmSetWarp(Packet):
    name = "Helm Set Warp "
    fields_desc = [LEIntField("warp_factor", 0)]
