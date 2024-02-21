from typing import Tuple, Optional

from scapy.fields import ByteField
from scapy.packet import Packet

from ..fields import (
    ArtemisSBSFloatField,
)
from ._properties import gen_fields


class EngineeringConsoleProperties(Packet):
    name = "Engineering Console Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("heat_level_1", None),
            ArtemisSBSFloatField("heat_level_2", None),
            ArtemisSBSFloatField("heat_level_3", None),
            ArtemisSBSFloatField("heat_level_4", None),
            ArtemisSBSFloatField("heat_level_5", None),
            ArtemisSBSFloatField("heat_level_6", None),
            ArtemisSBSFloatField("heat_level_7", None),
            ArtemisSBSFloatField("heat_level_8", None),
            ArtemisSBSFloatField("energy_allocation_1", None),
            ArtemisSBSFloatField("energy_allocation_2", None),
            ArtemisSBSFloatField("energy_allocation_3", None),
            ArtemisSBSFloatField("energy_allocation_4", None),
            ArtemisSBSFloatField("energy_allocation_5", None),
            ArtemisSBSFloatField("energy_allocation_6", None),
            ArtemisSBSFloatField("energy_allocation_7", None),
            ArtemisSBSFloatField("energy_allocation_8", None),
            ByteField("coolant_allocation_1", None),
            ByteField("coolant_allocation_2", None),
            ByteField("coolant_allocation_3", None),
            ByteField("coolant_allocation_4", None),
            ByteField("coolant_allocation_5", None),
            ByteField("coolant_allocation_6", None),
            ByteField("coolant_allocation_7", None),
            ByteField("coolant_allocation_8", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
