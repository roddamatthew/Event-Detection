from typing import Sequence

from scapy.fields import AnyField
from scapy.packet import Packet


class ServerHeartbeat(Packet):
    name = "Server Heartbeat "
    fields_desc: Sequence[AnyField] = []
