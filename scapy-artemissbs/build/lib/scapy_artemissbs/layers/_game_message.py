from scapy.packet import Packet

from ..fields import ArtemisSBSStrField


class GameMessage(Packet):
    name = "Game Message "
    fields_desc = [ArtemisSBSStrField("message", "")]
