from typing import Optional, Tuple

from scapy.fields import XLEIntField, ByteField
from scapy.packet import Packet

from ..fields import (
    ArtemisSBSFloatField,
    ArtemisSBSStrField,
    ArtemisSBSByteBooleanField,
)
from ._properties import gen_fields


class GenericMeshProperties(Packet):
    name = "Generic Mesh Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            XLEIntField("unknown_1p4", None),
            XLEIntField("unknown_1p5", None),
            XLEIntField("unknown_1p6", None),
            ArtemisSBSFloatField("roll", None),
            ArtemisSBSFloatField("pitch", None),
            ArtemisSBSFloatField("heading", None),
            ArtemisSBSFloatField("roll_delta", None),
            ArtemisSBSFloatField("pitch_delta", None),
            ArtemisSBSFloatField("heading_delta", None),
            ArtemisSBSStrField("name_", None),
            ArtemisSBSStrField("mesh_file", None),
            ArtemisSBSStrField("texture_file", None),
            ArtemisSBSFloatField("push_radius", None),
            ArtemisSBSByteBooleanField("block_shots", None),
            ArtemisSBSFloatField("scale", None),
            ArtemisSBSFloatField("red_color_channel", None),
            ArtemisSBSFloatField("blue_color_channel", None),
            ArtemisSBSFloatField("green_color_channel", None),
            ArtemisSBSFloatField("fore_shields", None),
            ArtemisSBSFloatField("aft_shields", None),
            ByteField("unknown_3p8", None),
            ArtemisSBSStrField("unknown_4p1", None),
            ArtemisSBSStrField("unknown_4p2", None),
            XLEIntField("unknown_4p3", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
