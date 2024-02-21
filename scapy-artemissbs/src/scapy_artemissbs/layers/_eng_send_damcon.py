from scapy.fields import LEIntField
from scapy.packet import Packet


class EngSendDamcon(Packet):
    name = "Engineering Send DAMCON "
    fields_desc = [
        LEIntField("team_number", 0),
        LEIntField("x", 0),
        LEIntField("y", 0),
        LEIntField("z", 0),
    ]
