from scapy.fields import LEIntField, LEIntEnumField
from scapy.packet import Packet

from .. import enums
from ..fields import ArtemisSBSFloatField


class BeamFired(Packet):
    name = "Beam Fired "
    fields_desc = [
        LEIntField("id", False),
        LEIntField("struct_type", 9),
        LEIntField("subtype", 0),
        LEIntField("beam_port_index", 0),
        LEIntEnumField("origin_object_type", 0, enums.object_type),
        LEIntEnumField("target_object_type", 0, enums.object_type),
        LEIntField("unknown", 0),
        LEIntField("origin_object_id", 0),
        LEIntField("target_object_id", 0),
        ArtemisSBSFloatField("target_x", 0),
        ArtemisSBSFloatField("target_y", 0),
        ArtemisSBSFloatField("target_z", 0),
        LEIntEnumField(
            "targeting_mode",
            0,
            enums.targeting_mode,
        ),
    ]
