from scapy.fields import LEIntField
from scapy.packet import Packet


class UnloadTube(Packet):
    name = "Unload Tube "
    fields_desc = [
        LEIntField("tube_index", 0),
    ]
