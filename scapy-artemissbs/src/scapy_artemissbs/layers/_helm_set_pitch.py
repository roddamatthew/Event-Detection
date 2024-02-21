from scapy.packet import Packet

from ..fields import ArtemisSBSFloatField


class HelmSetPitch(Packet):
    name = "Helm Set Pitch "
    fields_desc = [ArtemisSBSFloatField("pitch", 0)]
