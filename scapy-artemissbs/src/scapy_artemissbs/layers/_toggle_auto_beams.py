from scapy.fields import LEIntField
from scapy.packet import Packet


class ToggleAutoBeams(Packet):
    name = "Toggle Auto Beams "
    fields_desc = [LEIntField("unused", 0)]
