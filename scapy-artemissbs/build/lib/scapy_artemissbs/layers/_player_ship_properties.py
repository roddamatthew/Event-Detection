from typing import Tuple, Optional

from scapy.fields import LEIntField, ByteField, ByteEnumField
from scapy.packet import Packet

from .. import enums
from ..fields import (
    ArtemisSBSStrField,
    ArtemisSBSFloatField,
    ArtemisSBSByteBooleanField,
    ArtemisSBSShortBooleanField,
)
from ._properties import gen_fields


class PlayerShipProperties(Packet):
    name = "Player Ship Properties "
    fields_desc = gen_fields(
        [
            LEIntField("weapons_target", None),
            ArtemisSBSFloatField("impulse", None),
            ArtemisSBSFloatField("rudder", None),
            ArtemisSBSFloatField("top_speed", None),
            ArtemisSBSFloatField("turn_rate", None),
            ArtemisSBSByteBooleanField("auto_beams", None),
            ByteField("warp_factor", None),
            ArtemisSBSFloatField("energy_reserves", None),
            ArtemisSBSShortBooleanField("shields_up_or_down", None),
            LEIntField("unknown_2p2", None),
            LEIntField("hull_id", None),
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            ArtemisSBSFloatField("pitch", None),
            ArtemisSBSFloatField("roll", None),
            ArtemisSBSFloatField("heading", None),
            ArtemisSBSFloatField("velocity", None),
            ByteField("nebula_type", None),
            ArtemisSBSStrField("ship_name", None),
            ArtemisSBSFloatField("forward_shields", None),
            ArtemisSBSFloatField("forward_shields_max", None),
            ArtemisSBSFloatField("aft_shields", None),
            ArtemisSBSFloatField("aft_shields_max", None),
            LEIntField("last_docked_base", None),
            ByteEnumField("alert_status", None, enums.alert_status),
            ArtemisSBSFloatField("unknown_4p3", None),
            ByteEnumField("main_screen_view", None, enums.main_screen_view),
            ByteEnumField("beam_frequency", None, enums.beam_frequency),
            ByteField("available_coolant_or_missiles", None),
            LEIntField("science_target", None),
            LEIntField("captain_target", None),
            ByteEnumField("drive_type", None, enums.drive_type),
            LEIntField("scanning_id", None),
            ArtemisSBSFloatField("scanning_progress", None),
            ArtemisSBSByteBooleanField("reverse", None),
            ArtemisSBSFloatField("climb_or_dive", None),
            ByteField("side", None),
            LEIntField("map_visibility", None),
            ByteField("ship_index", None),
            LEIntField("capital_ship_object_id", None),
            ArtemisSBSFloatField("accent_color", None),
            ArtemisSBSFloatField("emergency_jump_cooldown", None),
            ByteEnumField("beacon_creature_type", None, enums.creature_type),
            ByteEnumField("beacon_mode", None, enums.beacon_mode),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s
