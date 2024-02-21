from typing import Optional, Tuple

from scapy.fields import ByteField, LEShortField, LEIntField
from scapy.packet import Packet

from ..fields import (
    ArtemisSBSByteBooleanField,
    ArtemisSBSStrField,
    ArtemisSBSFloatField,
    ArtemisSBSBooleanField,
)
from ._properties import gen_fields


class NPCShipProperties(Packet):
    name = "NPC Ship Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSStrField("name_", None),
            ArtemisSBSFloatField("throttle", None),
            ArtemisSBSFloatField("rudder", None),
            ArtemisSBSFloatField("max_impulse", None),
            ArtemisSBSFloatField("max_turn_rate", None),
            ArtemisSBSBooleanField("is_enemy", None),
            LEIntField("hull_id", None),
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            ArtemisSBSFloatField("pitch", None),
            ArtemisSBSFloatField("roll", None),
            ArtemisSBSFloatField("heading", None),
            ArtemisSBSFloatField("velocity", None),
            ArtemisSBSByteBooleanField("surrendered", None),
            ByteField("nebula_type", None),
            ArtemisSBSFloatField("forward_shields", None),
            ArtemisSBSFloatField("forward_shields_max", None),
            ArtemisSBSFloatField("aft_shields", None),
            ArtemisSBSFloatField("aft_shields_max", None),
            LEShortField("unknown_3p5", None),
            ByteField("fleet_number", None),
            LEIntField("special_abilities", None),
            LEIntField("active_special_abilities", None),
            LEIntField("single_scan", None),
            LEIntField("double_scan", None),
            LEIntField("map_visibility", None),
            ByteField("side", None),
            ByteField("unknown_4p5", None),
            ByteField("unknown_4p6", None),
            ByteField("unknown_4p7", None),
            ArtemisSBSFloatField("target_x", None),
            ArtemisSBSFloatField("target_y", None),
            ArtemisSBSFloatField("target_z", None),
            ByteField("tagged", None),
            ByteField("unknown_5p4", None),
            ArtemisSBSFloatField("ship_system_damage_1", None),
            ArtemisSBSFloatField("ship_system_damage_2", None),
            ArtemisSBSFloatField("ship_system_damage_3", None),
            ArtemisSBSFloatField("ship_system_damage_4", None),
            ArtemisSBSFloatField("ship_system_damage_5", None),
            ArtemisSBSFloatField("ship_system_damage_6", None),
            ArtemisSBSFloatField("ship_system_damage_7", None),
            ArtemisSBSFloatField("ship_system_damage_8", None),
            ArtemisSBSFloatField("beam_frequency_resistance_A", None),
            ArtemisSBSFloatField("beam_frequency_resistance_B", None),
            ArtemisSBSFloatField("beam_frequency_resistance_C", None),
            ArtemisSBSFloatField("beam_frequency_resistance_D", None),
            ArtemisSBSFloatField("beam_frequency_resistance_E", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
