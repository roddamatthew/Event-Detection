from scapy.fields import LEIntEnumField
from scapy.packet import Packet

from .. import enums


class SetMainScreen(Packet):
    name = "Set Main Screen "
    fields_desc = [LEIntEnumField("main_screen_view", 0, enums.main_screen_view)]
