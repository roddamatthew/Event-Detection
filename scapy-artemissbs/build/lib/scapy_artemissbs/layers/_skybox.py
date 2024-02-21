from scapy.fields import LEIntField
from scapy.packet import Packet


class Skybox(Packet):
    name = "Skybox "
    fields_desc = [
        LEIntField("skybox_id", 0),
    ]
