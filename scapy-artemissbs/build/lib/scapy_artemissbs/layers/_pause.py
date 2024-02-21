from scapy.packet import Packet

from ..fields import ArtemisSBSBooleanField


class Pause(Packet):
    name = "Pause "
    fields_desc = [
        ArtemisSBSBooleanField("paused", False),
    ]
