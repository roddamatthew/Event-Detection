from typing import Sequence

from scapy.fields import LEIntField
from scapy.packet import Packet


class ClimbDive(Packet):
    name = "Climb Dive "
    fields_desc = [LEIntField("direction", 0)]
