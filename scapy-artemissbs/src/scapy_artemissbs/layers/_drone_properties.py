from typing import Optional, Tuple

from scapy.fields import XLEIntField, LEIntField
from scapy.packet import Packet

from ..fields import (
    ArtemisSBSFloatField,
)
from ._properties import gen_fields


class DroneProperties(Packet):
    name = "Drone Properties"
    fields_desc = gen_fields(
        [
            XLEIntField("unknown_1p1", None),
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            ArtemisSBSFloatField("unknown_1p5", None),
            ArtemisSBSFloatField("unknown_1p6", None),
            ArtemisSBSFloatField("heading", None),
            LEIntField("side", None),
            ArtemisSBSFloatField("unknown_2p1", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
