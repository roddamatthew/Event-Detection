from typing import Optional, Tuple

from scapy.fields import LEIntEnumField, LEIntField, ByteEnumField
from scapy.packet import Packet

from .. import enums
from ..fields import (
    ArtemisSBSFloatField,
)
from ._properties import gen_fields


class AnomalyProperties(Packet):
    name = "Anomaly Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            LEIntEnumField("anomaly_type", None, enums.anomaly_type),
            LEIntField("scan", None),
            LEIntField("unknown", None),
            ByteEnumField("creature_type", None, enums.creature_type),
            ByteEnumField("beacon_mode", None, enums.beacon_mode),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
