from typing import Tuple, Optional

from scapy.fields import LEIntField, ByteField
from scapy.packet import Packet

from ..fields import ArtemisSBSStrField, ArtemisSBSFloatField
from ._properties import gen_fields


class BaseProperties(Packet):
    name = "BaseProperties "
    fields_desc = gen_fields(
        [
            ArtemisSBSStrField(
                "name_", None
            ),  # CANNOT HAVE NAME AS A FIELD FOR SOME REASON
            ArtemisSBSFloatField("shields", None),
            ArtemisSBSFloatField("max_shields", None),
            LEIntField("unknown_1p4", None),
            LEIntField("hull_id", None),
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            LEIntField("unknown_2p1", None),
            LEIntField("unknown_2p2", None),
            LEIntField("unknown_2p3", None),
            LEIntField("unknown_2p4", None),
            ByteField("unknown_2p5", None),
            ByteField("side", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
