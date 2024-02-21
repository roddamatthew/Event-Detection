from scapy.fields import LEIntField, LEIntEnumField
from scapy.packet import Packet

from .. import enums


class GameStart(Packet):
    name = "Game Start "
    fields_desc = [
        LEIntField("difficulty", 1),
        LEIntEnumField(
            "game_type",
            0,
            enums.game_type,
        ),
    ]
