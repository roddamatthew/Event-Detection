from typing import Sequence

from scapy.fields import AnyField
from scapy.packet import Packet


class EngResetCoolant(Packet):
    name = "Engineering Reset Coolant "
    fields_desc: Sequence[AnyField] = []
