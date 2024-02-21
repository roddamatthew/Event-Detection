from scapy.fields import XLEShortField
from scapy.packet import Packet

from ..fields import ArtemisSBSFlagsField, ArtemisSBSStrField


class CommsIncoming(Packet):
    name = "Comms Incoming "
    fields_desc = [
        # ArtemisSBSFlagsField("filters", 0, ["alert", "side", "status", "player", "station", "enemy", "friend"]),
        XLEShortField("filters", 0),
        ArtemisSBSStrField("sender", ""),
        ArtemisSBSStrField("message", ""),
    ]
