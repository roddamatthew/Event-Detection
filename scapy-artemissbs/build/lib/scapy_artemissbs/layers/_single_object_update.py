from scapy.fields import ByteEnumField, LEIntField
from scapy.packet import Packet

from .. import enums


class SingleObjectUpdate(Packet):
    name = "Single Object Update "
    fields_desc = [
        ByteEnumField("object_type", 0, enums.object_type),
        LEIntField("object_id", 0),
    ]
