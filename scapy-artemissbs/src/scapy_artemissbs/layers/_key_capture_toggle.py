from scapy.packet import Packet

from ..fields import ArtemisSBSByteBooleanField


class KeyCaptureToggle(Packet):
    name = "Key Capture Toggle "
    fields_desc = [
        ArtemisSBSByteBooleanField("capture", False),
    ]
