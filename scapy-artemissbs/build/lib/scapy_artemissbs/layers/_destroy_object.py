from scapy.fields import ByteEnumField, LEIntField
from scapy.packet import Packet

from .. import enums


class DestroyObject(Packet):
    name = "Destroy Object "
    fields_desc = [
        ByteEnumField("object_type", 0, enums.object_type),
        LEIntField("object_id", 0),
    ]
