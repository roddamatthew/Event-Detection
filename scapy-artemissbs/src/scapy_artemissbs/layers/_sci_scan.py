from scapy.fields import LEIntField
from scapy.packet import Packet


class SciScan(Packet):
    name = "Science Scan "
    fields_desc = [LEIntField("target_id", 0)]
