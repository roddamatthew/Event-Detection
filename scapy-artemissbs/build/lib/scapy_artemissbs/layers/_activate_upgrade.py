from scapy.fields import LEIntEnumField
from scapy.packet import Packet

from .. import enums


class ActivateUpgrade(Packet):
    name = "Activate Upgrade "
    fields_desc = [
        LEIntEnumField("upgrade", 0, enums.upgrades),
    ]
