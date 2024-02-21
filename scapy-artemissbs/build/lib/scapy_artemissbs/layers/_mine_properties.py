from typing import Optional, Tuple

from scapy.packet import Packet

from ..fields import (
    ArtemisSBSFloatField,
)
from ._properties import gen_fields


class MineProperties(Packet):
    name = "Mine Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
