from scapy.fields import LEIntField
from scapy.packet import Packet


class SetWeaponsTarget(Packet):
    name = "Set Weapons Target "
    fields_desc = [LEIntField("target_id", 1)]
