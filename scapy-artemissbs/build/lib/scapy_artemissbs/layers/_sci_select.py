from scapy.fields import LEIntField
from scapy.packet import Packet


class SciSelect(Packet):
    name = "Science Select "
    fields_desc = [LEIntField("target_id", 0)]
