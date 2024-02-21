from typing import Optional, Tuple

from scapy.fields import LEIntField, LEIntEnumField
from scapy.packet import Packet

from .. import enums
from ..fields import (
    ArtemisSBSFloatField,
)
from ._properties import gen_fields


class TorpedoProperties(Packet):
    name = "Torpedo Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            ArtemisSBSFloatField("delta_x", None),
            ArtemisSBSFloatField("delta_y", None),
            ArtemisSBSFloatField("delta_z", None),
            LEIntField("unknown_1p7", None),
            LEIntEnumField("ordnance_type", None, enums.ordnance_type),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
