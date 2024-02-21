from scapy.fields import PacketListField, LEIntField
from scapy.packet import List, Optional, Packet, Type

from ._single_object_update import SingleObjectUpdate


def _next_cls_cb(
    pkt: Packet, lst: List[Packet], cur: Optional[Packet], remain: str
) -> Optional[Type[Packet]]:
    return None if (not remain or remain[0] == 0) else SingleObjectUpdate


class ObjectUpdate(Packet):
    name = "Object Update Packet "
    fields_desc = [
        PacketListField("updates", [], next_cls_cb=_next_cls_cb),
        LEIntField("padding", 0),
    ]
