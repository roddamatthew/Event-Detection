from scapy.fields import LEIntField
from scapy.packet import Packet

from ..fields import ArtemisSBSStrField


class Tag(Packet):
    name = "Tag "
    fields_desc = [
        LEIntField("object_id", 0),
        LEIntField("unknown", 0),
        ArtemisSBSStrField("tagger", ""),
        ArtemisSBSStrField("date", ""),
    ]
