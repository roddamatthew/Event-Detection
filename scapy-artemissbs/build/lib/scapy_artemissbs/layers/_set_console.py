from scapy.fields import LEIntEnumField
from scapy.packet import Packet

from .. import enums
from ..fields import ArtemisSBSBooleanField


class SetConsole(Packet):
    name = "Set Console "
    fields_desc = [
        LEIntEnumField("console_type", 0, enums.console_type),
        ArtemisSBSBooleanField("selected", False),
    ]
