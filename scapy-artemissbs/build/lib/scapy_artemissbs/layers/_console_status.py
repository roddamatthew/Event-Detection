from scapy.fields import LEIntField, ByteEnumField
from scapy.packet import Packet

from .. import enums


class ConsoleStatus(Packet):
    name = "Console Status "
    fields_desc = [
        LEIntField("ship_number", 0),
        ByteEnumField("main_screen", 0, enums.console_status),
        ByteEnumField("helm", 0, enums.console_status),
        ByteEnumField("weapons", 0, enums.console_status),
        ByteEnumField("engineering", 0, enums.console_status),
        ByteEnumField("science", 0, enums.console_status),
        ByteEnumField("communications", 0, enums.console_status),
        ByteEnumField("single_seat_craft", 0, enums.console_status),
        ByteEnumField("data", 0, enums.console_status),
        ByteEnumField("observer", 0, enums.console_status),
        ByteEnumField("captains_map", 0, enums.console_status),
        ByteEnumField("game_master", 0, enums.console_status),
    ]
