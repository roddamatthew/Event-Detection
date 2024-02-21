from scapy.fields import LEIntField
from scapy.packet import Packet


class HelmRequestDock(Packet):
    name = "Helm Request Dock "
    fields_desc = [LEIntField("single_seat_craft_id", 0)]
