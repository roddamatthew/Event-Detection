from typing import Optional, Tuple

from scapy.fields import ByteField
from scapy.packet import Packet

from ..fields import (
    ArtemisSBSFloatField,
)
from ._properties import gen_fields


class NebulaProperties(Packet):
    name = "Nebula Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            ArtemisSBSFloatField("red_color_channel", None),
            ArtemisSBSFloatField("green_color_channel", None),
            ArtemisSBSFloatField("blue_color_channel", None),
            ByteField("type", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
