from typing import Sequence

from scapy.fields import AnyField
from scapy.packet import Packet


class ClientHeartbeat(Packet):
    name = "Client Heartbeat "
    fields_desc: Sequence[AnyField] = []
