from typing import Any, Optional

from scapy.fields import Field, ConditionalField
from scapy.packet import Packet


class PropertyField(ConditionalField):
    def __init__(self, fld: Field[Any, Any]) -> None:
        super().__init__(fld, lambda pkt: pkt.flags and fld.name in pkt.flags)

    def addfield(self, pkt: Packet, s: bytes, val: Any) -> bytes:
        return s if val is None else self.fld.addfield(pkt, s, val)

    def i2h(self, pkt: Optional[Packet], val: Any):
        return self.fld.i2h(pkt, val)
