from scapy.fields import LEIntField
from scapy.packet import Packet


class ToggleShields(Packet):
    name = "Toggle Shields "
    fields_desc = [LEIntField("padding", 0)]
