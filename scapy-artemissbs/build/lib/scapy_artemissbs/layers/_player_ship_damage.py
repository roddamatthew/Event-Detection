from scapy.fields import LEIntField
from scapy.packet import Packet

from ..fields import ArtemisSBSFloatField


class PlayerShipDamage(Packet):
    name = "Player Ship Damage "
    fields_desc = [
        LEIntField("ship_index", 0),
        ArtemisSBSFloatField("duration", 0),
    ]
