from scapy.fields import LEIntEnumField
from scapy.packet import Packet

from .. import enums


class SetBeamFreq(Packet):
    name = "Set Beam Frequency "
    fields_desc = [LEIntEnumField("beam_frequency", 0, enums.beam_frequency)]
