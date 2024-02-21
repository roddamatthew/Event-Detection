from typing import Optional, Tuple

from scapy.fields import ByteField, ByteEnumField
from scapy.packet import Packet

from .. import enums
from ..fields import (
    ArtemisSBSFloatField,
)
from ._properties import gen_fields


class WeaponsConsoleProperties(Packet):
    name = "Weapons Console Properties "
    fields_desc = gen_fields(
        [
            ByteField("ordnance_count_1", None),
            ByteField("ordnance_count_2", None),
            ByteField("ordnance_count_3", None),
            ByteField("ordnance_count_4", None),
            ByteField("ordnance_count_5", None),
            ByteField("ordnance_count_6", None),
            ByteField("ordnance_count_7", None),
            ByteField("ordnance_count_8", None),
            ArtemisSBSFloatField("tube_load_time_1", None),
            ArtemisSBSFloatField("tube_load_time_2", None),
            ArtemisSBSFloatField("tube_load_time_3", None),
            ArtemisSBSFloatField("tube_load_time_4", None),
            ArtemisSBSFloatField("tube_load_time_5", None),
            ArtemisSBSFloatField("tube_load_time_6", None),
            ByteEnumField("tube_status_1", None, enums.tube_status),
            ByteEnumField("tube_status_2", None, enums.tube_status),
            ByteEnumField("tube_status_3", None, enums.tube_status),
            ByteEnumField("tube_status_4", None, enums.tube_status),
            ByteEnumField("tube_status_5", None, enums.tube_status),
            ByteEnumField("tube_status_6", None, enums.tube_status),
            ByteEnumField("ordnance_type_1", None, enums.ordnance_type),
            ByteEnumField("ordnance_type_2", None, enums.ordnance_type),
            ByteEnumField("ordnance_type_3", None, enums.ordnance_type),
            ByteEnumField("ordnance_type_4", None, enums.ordnance_type),
            ByteEnumField("ordnance_type_5", None, enums.ordnance_type),
            ByteEnumField("ordnance_type_6", None, enums.ordnance_type),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
