from scapy.packet import Packet

from ..fields import ArtemisSBSFloatField


class HelmSetImpulse(Packet):
    name = "Helm Set Impulse "
    fields_desc = [ArtemisSBSFloatField("throttle", 0)]
