from scapy.fields import LEIntField, ByteEnumField
from scapy.packet import Packet

from ..fields import ArtemisSBSStrField

from .. import enums


class Intel(Packet):
    name = "Intel Packet "
    fields_desc = [
        LEIntField("object_id", 0),
        ByteEnumField("intel_type", 0, enums.intel_type),
        ArtemisSBSStrField("intel", ""),
    ]
