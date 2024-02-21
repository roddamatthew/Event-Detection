from scapy.fields import PacketListField
from scapy.packet import Packet

from ._ship_settings import ShipSettings


class AllShipSettings(Packet):
    name = "All Ship Settings "
    fields_desc = [PacketListField("ships", [], ShipSettings)]
