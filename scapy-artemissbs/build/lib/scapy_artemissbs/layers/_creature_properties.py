from typing import Optional, Tuple

from scapy.fields import XLEIntField, LEIntEnumField, LEIntField, XByteField
from scapy.packet import Packet

from .. import enums
from ..fields import (
    ArtemisSBSFloatField,
    ArtemisSBSStrField,
)
from ._properties import gen_fields


class CreatureProperties(Packet):
    name = "Creature Properties"
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            ArtemisSBSStrField("name_", None),
            ArtemisSBSFloatField("heading", None),
            ArtemisSBSFloatField("pitch", None),
            ArtemisSBSFloatField("roll", None),
            LEIntEnumField("creature_type", None, enums.creature_type),
            LEIntField("scan", None),
            XLEIntField("unknown_2p2", None),
            XLEIntField("unknown_2p3", None),
            XLEIntField("unknown_2p4", None),
            XLEIntField("unknown_2p5", None),
            XLEIntField("unknown_2p6", None),
            ArtemisSBSFloatField("health", None),
            ArtemisSBSFloatField("max_health", None),
            XByteField("unknown_3p1", None),
            XLEIntField("unknown_3p2", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
