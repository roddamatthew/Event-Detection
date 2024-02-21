from scapy.packet import Packet

from ..fields import ArtemisSBSFloatField


class HelmSetSteering(Packet):
    name = "Helm Set Steering "
    fields_desc = [ArtemisSBSFloatField("rudder", 0.5)]
