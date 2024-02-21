from typing import Tuple, Union, TypeVar

from scapy.packet import Packet

from ._artemissbs_flags_field import ArtemisSBSFlagsField


I = TypeVar("I")


class PropertyFlagsField(ArtemisSBSFlagsField):
    def addfield(
        self, pkt: Packet, s: Union[Tuple[bytes, int, int], bytes], ival: I
    ) -> Union[Tuple[bytes, int, int], bytes]:
        if ival is None:
            ival = self.any2i(
                pkt,
                [attr for attr in self.names if getattr(pkt, attr, None) is not None],
            )
        return super().addfield(pkt, s, ival)
