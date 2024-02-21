from typing import Tuple, Optional

from scapy.fields import LEIntField, PacketListField
from scapy.packet import Packet

from ..fields import ArtemisSBSStrField


class FighterBay(Packet):
    fields_desc = [
        LEIntField("object_id", 0),
        LEIntField("bay_number", 0),
        ArtemisSBSStrField("fighter_name", ""),
        ArtemisSBSStrField("fight_class_name", ""),
        LEIntField("refit_time", 0),
    ]

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


def next_cls_cb(pkt, lst, cur, remain):
    return None if remain == b"\x00\x00\x00\x00" else FighterBay


class FighterBayStatus(Packet):
    name = "Fighter Bay Status "
    fields_desc = [
        PacketListField(
            "bays",
            [],
            next_cls_cb=next_cls_cb,
        )
    ]

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s[4:]
