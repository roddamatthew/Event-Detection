from scapy.fields import LEIntField
from scapy.packet import Packet


class TogglePerspective(Packet):
    name = "Toggle Perspective "
    fields_desc = [LEIntField("unused", 0)]
