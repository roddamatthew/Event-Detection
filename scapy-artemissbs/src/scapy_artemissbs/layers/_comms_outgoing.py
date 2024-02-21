from scapy.fields import LEIntEnumField, LEIntField
from scapy.packet import Packet

from .. import enums


class CommsOutgoing(Packet):
    name = "Comms Outgoing "
    fields_desc = [
        LEIntEnumField("comm_target_type", 0, enums.comm_target_type),
        LEIntField("recipient_id", 0),
        LEIntField("message", 0),
        LEIntField("target_object_id", 0),
        LEIntField("unknown", 0),
    ]
