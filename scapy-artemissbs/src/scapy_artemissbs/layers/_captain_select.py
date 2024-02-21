from scapy.fields import LEIntField
from scapy.packet import Packet, bind_layers


class CaptainSelect(Packet):
    name = "Captain Select "
    fields_desc = [
        LEIntField("target_id", 0),
    ]
