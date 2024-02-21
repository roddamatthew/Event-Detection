import struct
from typing import Optional, Sequence, Tuple, List

from scapy.fields import (
    AnyField,
    ByteEnumField,
    ByteField,
    Field,
    LEIntEnumField,
    LEIntField,
    LEShortField,
    PacketListField,
    XByteField,
    XLEIntField,
    XLEShortField,
)
from scapy.packet import Packet, bind_layers

from . import enums
from .fields import (
    ArtemisSBSBooleanField,
    ArtemisSBSByteBooleanField,
    ArtemisSBSFloatField,
    ArtemisSBSShortBooleanField,
    ArtemisSBSStrField,
    ConstantField,
    DAMCONTeamStatusField,
    FlaggedField,
    MetaField,
    PropertyField,
    PropertyFlagsField,
    SystemGridStatusField,
    XLEVarIntField,
    VersionField,
)


def gen_fields(fields: Sequence[Field]):
    flags_field = PropertyFlagsField("flags", None, [field.name for field in fields])
    # flags_checker = _FlagsChecker(flags_field)
    wrapped_fields: List[Field] = [PropertyField(field) for field in fields]
    fields_desc: Sequence[Field] = [flags_field] + wrapped_fields
    return fields_desc


class ActivateUpgrade(Packet):
    name = "Activate Upgrade "
    fields_desc = [
        LEIntEnumField("upgrade", 0, enums.upgrades),
    ]


class ShipSettings(Packet):
    fields_desc = [
        LEIntEnumField("drive_type", 0, enums.drive_type),
        LEIntField("hull_id", 0),
        ArtemisSBSFloatField("accent_color", 0),
        FlaggedField(
            ArtemisSBSBooleanField("has_name", False), ArtemisSBSStrField("name", None)
        ),
    ]

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class AllShipSettings(Packet):
    name = "All Ship Settings "
    fields_desc = [PacketListField("ships", [], ShipSettings)]


class AnomalyProperties(Packet):
    name = "Anomaly Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            LEIntEnumField("anomaly_type", None, enums.anomaly_type),
            LEIntField("scan", None),
            LEIntField("unknown", None),
            ByteEnumField("creature_type", None, enums.creature_type),
            ByteEnumField("beacon_mode", None, enums.beacon_mode),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class ArtemisSBS(Packet):
    name = "Artemis Spaceship Bridge Simulator "
    fields_desc = [
        ConstantField(XLEIntField("header", 0xDEADBEEF)),
        LEIntField("len", None),
        LEIntEnumField("origin", 1, {1: "server", 2: "client"}),
        ConstantField(LEIntField("padding", 0)),
        LEIntField("remaining", None),
        LEIntEnumField(
            "internal_type",
            0x80803DF9,
            enums.internal_type,
        ),
        XLEVarIntField(
            "internal_subtype",
            None,
            lambda pkt: enums.subtype_lengths.get(pkt.internal_type, 0),
        ),
        MetaField(
            "type",
            "",
            lambda pkt: enums.packet_type[
                (pkt.origin, pkt.internal_type, pkt.internal_subtype)
            ],
        ),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.type = None

    def post_build(self, p, pay):
        if self.len is None:
            p = p[:4] + struct.pack("<I", len(p + pay)) + p[8:]
        if self.remaining is None:
            p = p[:16] + struct.pack("<I", len(p + pay) - 20) + p[20:]
        return p + pay

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        payload_len = self.len - (24 + enums.subtype_lengths.get(self.internal_type, 0))
        payload, padding = s[:payload_len], s[payload_len:]
        return payload, padding

    def _update_type(self, val, fld):
        flds = ["origin", "internal_type", "internal_subtype"]
        key = tuple(val if f == fld.name else getattr(self, fld) for f in flds)
        self.type = enums.packet_type(key)


class ArtemisSBSStream(Packet):
    name = "Artemis Spaceship Bridge Simulator Stream"
    fields_desc = [
        PacketListField(
            "packets",
            [],
            ArtemisSBS,
        )
    ]

    @classmethod
    def tcp_reassemble(cls, data, metadata):
        length = metadata.get("length", 0)
        while length < len(data):
            length = length + struct.unpack("<I", data[length + 4 : length + 8])[0]
        if length == len(data):
            return cls(data)
        metadata["length"] = length
        return None


class AsteroidProperties(Packet):
    name = "Asteroid Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class BaseProperties(Packet):
    name = "BaseProperties "
    fields_desc = gen_fields(
        [
            ArtemisSBSStrField(
                "name_", None
            ),  # CANNOT HAVE NAME AS A FIELD FOR SOME REASON
            ArtemisSBSFloatField("shields", None),
            ArtemisSBSFloatField("max_shields", None),
            LEIntField("unknown_1p4", None),
            LEIntField("hull_id", None),
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            LEIntField("unknown_2p1", None),
            LEIntField("unknown_2p2", None),
            LEIntField("unknown_2p3", None),
            LEIntField("unknown_2p4", None),
            ByteField("unknown_2p5", None),
            ByteField("side", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


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


class BlackHoleProperties(Packet):
    name = "Black Hole Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class CaptainSelect(Packet):
    name = "Captain Select "
    fields_desc = [
        LEIntField("target_id", 0),
    ]


class ClientHeartbeat(Packet):
    name = "Client Heartbeat "
    fields_desc: Sequence[AnyField] = []


class ClimbDive(Packet):
    name = "Climb Dive "
    fields_desc = [LEIntField("direction", 0)]


class CloakDecloak(Packet):
    name = "Cloak/Decloak "
    fields_desc = [
        ArtemisSBSFloatField("x", 0),
        ArtemisSBSFloatField("y", 0),
        ArtemisSBSFloatField("z", 0),
    ]


class CommsIncoming(Packet):
    name = "Comms Incoming "
    fields_desc = [
        # ArtemisSBSFlagsField("filters", 0, ["alert", "side", "status", "player", "station", "enemy", "friend"]),
        XLEShortField("filters", 0),
        ArtemisSBSStrField("sender", ""),
        ArtemisSBSStrField("message", ""),
    ]


class CommsOutgoing(Packet):
    name = "Comms Outgoing "
    fields_desc = [
        LEIntEnumField("comm_target_type", 0, enums.comm_target_type),
        LEIntField("recipient_id", 0),
        LEIntField("message", 0),
        LEIntField("target_object_id", 0),
        LEIntField("unknown", 0),
    ]


class ConsoleStatus(Packet):
    name = "Console Status "
    fields_desc = [
        LEIntField("ship_number", 0),
        ByteEnumField("main_screen", 0, enums.console_status),
        ByteEnumField("helm", 0, enums.console_status),
        ByteEnumField("weapons", 0, enums.console_status),
        ByteEnumField("engineering", 0, enums.console_status),
        ByteEnumField("science", 0, enums.console_status),
        ByteEnumField("communications", 0, enums.console_status),
        ByteEnumField("single_seat_craft", 0, enums.console_status),
        ByteEnumField("data", 0, enums.console_status),
        ByteEnumField("observer", 0, enums.console_status),
        ByteEnumField("captains_map", 0, enums.console_status),
        ByteEnumField("game_master", 0, enums.console_status),
    ]


class CreatureProperties(Packet):
    name = "Creature Properties"
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            ArtemisSBSStrField("name_", None),
            ArtemisSBSFloatField("heading", None),
            ArtemisSBSFloatField("pitch", None),
            ArtemisSBSFloatField("roll", None),
            LEIntEnumField("creature_type", None, enums.creature_type),
            LEIntField("scan", None),
            XLEIntField("unknown_2p2", None),
            XLEIntField("unknown_2p3", None),
            XLEIntField("unknown_2p4", None),
            XLEIntField("unknown_2p5", None),
            XLEIntField("unknown_2p6", None),
            ArtemisSBSFloatField("health", None),
            ArtemisSBSFloatField("max_health", None),
            XByteField("unknown_3p1", None),
            XLEIntField("unknown_3p2", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class DestroyObject(Packet):
    name = "Destroy Object "
    fields_desc = [
        ByteEnumField("object_type", 0, enums.object_type),
        LEIntField("object_id", 0),
    ]


class Detonation(Packet):
    name = "Detonation "
    fields_desc = [
        LEIntEnumField("object_type", 0, enums.object_type),
        LEIntField("object_id", 0),
    ]


class Docked(Packet):
    name = "Docked "
    fields_desc = [LEIntField("object_id", 0)]


class DroneProperties(Packet):
    name = "Drone Properties"
    fields_desc = gen_fields(
        [
            XLEIntField("unknown_1p1", None),
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            ArtemisSBSFloatField("unknown_1p5", None),
            ArtemisSBSFloatField("unknown_1p6", None),
            ArtemisSBSFloatField("heading", None),
            LEIntField("side", None),
            ArtemisSBSFloatField("unknown_2p1", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class EngGridUpdate(Packet):
    name = "Engineering Grid Update "
    fields_desc = [
        ArtemisSBSByteBooleanField("full_status", False),
        SystemGridStatusField("system_grid_status", []),
        DAMCONTeamStatusField("damcon_team_status", []),
    ]


class EngResetCoolant(Packet):
    name = "Engineering Reset Coolant "
    fields_desc: Sequence[AnyField] = []


class EngSendDamcon(Packet):
    name = "Engineering Send DAMCON "
    fields_desc = [
        LEIntField("team_number", 0),
        LEIntField("x", 0),
        LEIntField("y", 0),
        LEIntField("z", 0),
    ]


class EngSetCoolant(Packet):
    name = "Engineering Set Coolant "
    fields_desc = [
        LEIntEnumField("ship_system", 0, enums.ship_system),
        LEIntField("value", 0),
        LEIntField("unknown1", 0),
        LEIntField("unknown2", 0),
    ]


class EngSetEnergy(Packet):
    name = "Engineering Set Energy "
    fields_desc = [
        ArtemisSBSFloatField("value", 0.5),
        LEIntEnumField("ship_system", 0, enums.ship_system),
    ]


class EngineeringConsoleProperties(Packet):
    name = "Engineering Console Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("heat_level_1", None),
            ArtemisSBSFloatField("heat_level_2", None),
            ArtemisSBSFloatField("heat_level_3", None),
            ArtemisSBSFloatField("heat_level_4", None),
            ArtemisSBSFloatField("heat_level_5", None),
            ArtemisSBSFloatField("heat_level_6", None),
            ArtemisSBSFloatField("heat_level_7", None),
            ArtemisSBSFloatField("heat_level_8", None),
            ArtemisSBSFloatField("energy_allocation_1", None),
            ArtemisSBSFloatField("energy_allocation_2", None),
            ArtemisSBSFloatField("energy_allocation_3", None),
            ArtemisSBSFloatField("energy_allocation_4", None),
            ArtemisSBSFloatField("energy_allocation_5", None),
            ArtemisSBSFloatField("energy_allocation_6", None),
            ArtemisSBSFloatField("energy_allocation_7", None),
            ArtemisSBSFloatField("energy_allocation_8", None),
            ByteField("coolant_allocation_1", None),
            ByteField("coolant_allocation_2", None),
            ByteField("coolant_allocation_3", None),
            ByteField("coolant_allocation_4", None),
            ByteField("coolant_allocation_5", None),
            ByteField("coolant_allocation_6", None),
            ByteField("coolant_allocation_7", None),
            ByteField("coolant_allocation_8", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class Explosion(Packet):
    name = "Explosion "
    fields_desc = [
        LEIntEnumField("object_type", 0, enums.object_type),
        LEIntField("object_id", 0),
    ]


class FighterBay(Packet):
    fields_desc = [
        LEIntField("object_id", 0),
        LEIntField("bay_number", 0),
        ArtemisSBSStrField("fighter_name", ""),
        ArtemisSBSStrField("fight_class_name", ""),
        LEIntField("refit_time", 0),
    ]

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class FighterBayStatus(Packet):
    name = "Fighter Bay Status "
    fields_desc = [
        PacketListField(
            "bays",
            [],
            next_cls_cb=lambda pkt, lst, cur, remain: None
            if remain == b"\x00\x00\x00\x00"
            else FighterBay,
        )
    ]

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s[4:]


class FireTube(Packet):
    name = "Fire Tube "
    fields_desc = [LEIntField("tube_index", 0)]


class GameMasterSelectLocation(Packet):
    name = "Game Master Select Location "
    fields_desc = [
        ArtemisSBSFloatField("z", 0),
        ArtemisSBSFloatField("y", 0),
        ArtemisSBSFloatField("x", 0),
    ]


class GameMessage(Packet):
    name = "Game Message "
    fields_desc = [ArtemisSBSStrField("message", "")]


class GameStart(Packet):
    name = "Game Start "
    fields_desc = [
        LEIntField("difficulty", 1),
        LEIntEnumField(
            "game_type",
            0,
            enums.game_type,
        ),
    ]


class GenericMeshProperties(Packet):
    name = "Generic Mesh Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            XLEIntField("unknown_1p4", None),
            XLEIntField("unknown_1p5", None),
            XLEIntField("unknown_1p6", None),
            ArtemisSBSFloatField("roll", None),
            ArtemisSBSFloatField("pitch", None),
            ArtemisSBSFloatField("heading", None),
            ArtemisSBSFloatField("roll_delta", None),
            ArtemisSBSFloatField("pitch_delta", None),
            ArtemisSBSFloatField("heading_delta", None),
            ArtemisSBSStrField("name_", None),
            ArtemisSBSStrField("mesh_file", None),
            ArtemisSBSStrField("texture_file", None),
            ArtemisSBSFloatField("push_radius", None),
            ArtemisSBSByteBooleanField("block_shots", None),
            ArtemisSBSFloatField("scale", None),
            ArtemisSBSFloatField("red_color_channel", None),
            ArtemisSBSFloatField("blue_color_channel", None),
            ArtemisSBSFloatField("green_color_channel", None),
            ArtemisSBSFloatField("fore_shields", None),
            ArtemisSBSFloatField("aft_shields", None),
            ByteField("unknown_3p8", None),
            ArtemisSBSStrField("unknown_4p1", None),
            ArtemisSBSStrField("unknown_4p2", None),
            XLEIntField("unknown_4p3", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class HelmJump(Packet):
    name = "Helm Jump "
    fields_desc = [
        ArtemisSBSFloatField("bearing", 0),
        ArtemisSBSFloatField("distance", 0),
    ]


class HelmRequestDock(Packet):
    name = "Helm Request Dock "
    fields_desc = [LEIntField("single_seat_craft_id", 0)]


class HelmSetImpulse(Packet):
    name = "Helm Set Impulse "
    fields_desc = [ArtemisSBSFloatField("throttle", 0)]


class HelmSetPitch(Packet):
    name = "Helm Set Pitch "
    fields_desc = [ArtemisSBSFloatField("pitch", 0)]


class HelmSetSteering(Packet):
    name = "Helm Set Steering "
    fields_desc = [ArtemisSBSFloatField("rudder", 0.5)]


class HelmSetWarp(Packet):
    name = "Helm Set Warp "
    fields_desc = [LEIntField("warp_factor", 0)]


class HelmToggleReverse(Packet):
    name = "Helm Toggle Reverse "
    fields_desc = [LEIntField("unused", 0)]


class Intel(Packet):
    name = "Intel Packet "
    fields_desc = [
        LEIntField("object_id", 0),
        ByteEnumField("intel_type", 0, enums.intel_type),
        ArtemisSBSStrField("intel", ""),
    ]


class KeyCaptureToggle(Packet):
    name = "Key Capture Toggle "
    fields_desc = [
        ArtemisSBSByteBooleanField("capture", False),
    ]


class LoadTube(Packet):
    name = "Load Tube "
    fields_desc = [
        LEIntField("tube_index", 0),
        LEIntEnumField("ordnance_type", 0, enums.ordnance_type),
        LEIntField("unknown1", 0),
        LEIntField("unknown2", 0),
    ]


class MineProperties(Packet):
    name = "Mine Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class NebulaProperties(Packet):
    name = "Nebula Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            ArtemisSBSFloatField("red_color_channel", None),
            ArtemisSBSFloatField("green_color_channel", None),
            ArtemisSBSFloatField("blue_color_channel", None),
            ByteField("type", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


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


class ObjectUpdate(Packet):
    name = "Object Update Packet "
    fields_desc = [
        PacketListField(
            "updates",
            [],
            next_cls_cb=lambda pkt, lst, cur, remain: None
            if (not remain or remain[0] == 0)
            else SingleObjectUpdate,
        ),
        LEIntField("padding", 0),
    ]


class Pause(Packet):
    name = "Pause "
    fields_desc = [
        ArtemisSBSBooleanField("paused", False),
    ]


class PlayerShipDamage(Packet):
    name = "Player Ship Damage "
    fields_desc = [
        LEIntField("ship_index", 0),
        ArtemisSBSFloatField("duration", 0),
    ]


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


class PlayerShipUpgradesProperties(Packet):
    name = "Player Ship Upgrades Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSByteBooleanField("active_infusion_p_coils", None),
            ArtemisSBSByteBooleanField("active_hydrogen_ram", None),
            ArtemisSBSByteBooleanField("active_tauron_focusers", None),
            ArtemisSBSByteBooleanField("active_carapaction_coils", None),
            ArtemisSBSByteBooleanField("active_polyphasic_capacitors", None),
            ArtemisSBSByteBooleanField("active_cetrocite_crystals", None),
            ArtemisSBSByteBooleanField("active_lateral_array", None),
            ArtemisSBSByteBooleanField("active_ecm_starpulse", None),
            ArtemisSBSByteBooleanField("active_double_agent", None),
            ArtemisSBSByteBooleanField("active_wartime_production", None),
            ArtemisSBSByteBooleanField("active_infusion_p_coils_perm", None),
            ArtemisSBSByteBooleanField("active_protonic_verniers", None),
            ArtemisSBSByteBooleanField("active_tauron_focusers_perm", None),
            ArtemisSBSByteBooleanField("active_regenerative_pau_grids", None),
            ArtemisSBSByteBooleanField("active_veteran_damcon_teams", None),
            ArtemisSBSByteBooleanField("active_cetrocite_heatsinks", None),
            ArtemisSBSByteBooleanField("active_tachyon_scanners", None),
            ArtemisSBSByteBooleanField("active_gridscan_overload", None),
            ArtemisSBSByteBooleanField("active_override_authorization", None),
            ArtemisSBSByteBooleanField("active_resupply_imperatives", None),
            ArtemisSBSByteBooleanField("active_patrol_group", None),
            ArtemisSBSByteBooleanField("active_fast_supply", None),
            ArtemisSBSByteBooleanField("active_vanguard_refit_helm", None),
            ArtemisSBSByteBooleanField("active_vanguard_refit_weap", None),
            ArtemisSBSByteBooleanField("active_vanguard_refit_comm", None),
            ArtemisSBSByteBooleanField("active_vanguard_refit_station", None),
            ArtemisSBSByteBooleanField("active_vanguard_refit_eng", None),
            ArtemisSBSByteBooleanField("active_vanguard_refit_systems", None),
            ByteField("count_infusion_p_coils", None),
            ByteField("count_hydrogen_ram", None),
            ByteField("count_tauron_focusers", None),
            ByteField("count_carapaction_coils", None),
            ByteField("count_polyphasic_capacitors", None),
            ByteField("count_cetrocite_crystals", None),
            ByteField("count_lateral_array", None),
            ByteField("count_ecm_starpulse", None),
            ByteField("count_double_agent", None),
            ByteField("count_wartime_production", None),
            ByteField("count_infusion_p_coils_perm", None),
            ByteField("count_protonic_verniers", None),
            ByteField("count_tauron_focusers_perm", None),
            ByteField("count_regenerative_pau_grids", None),
            ByteField("count_veteran_damcon_teams", None),
            ByteField("count_cetrocite_heatsinks", None),
            ByteField("count_tachyon_scanners", None),
            ByteField("count_gridscan_overload", None),
            ByteField("count_override_authorization", None),
            ByteField("count_resupply_imperatives", None),
            ByteField("count_patrol_group", None),
            ByteField("count_fast_supply", None),
            ByteField("count_vanguard_refit_helm", None),
            ByteField("count_vanguard_refit_weap", None),
            ByteField("count_vanguard_refit_comm", None),
            ByteField("count_vanguard_refit_station", None),
            ByteField("count_vanguard_refit_eng", None),
            ByteField("count_vanguard_refit_systems", None),
            LEShortField("time_infusion_p_coils", None),
            LEShortField("time_hydrogen_ram", None),
            LEShortField("time_tauron_focusers", None),
            LEShortField("time_carapaction_coils", None),
            LEShortField("time_polyphasic_capacitors", None),
            LEShortField("time_cetrocite_crystals", None),
            LEShortField("time_lateral_array", None),
            LEShortField("time_ecm_starpulse", None),
            LEShortField("time_double_agent", None),
            LEShortField("time_wartime_production", None),
            LEShortField("time_infusion_p_coils_perm", None),
            LEShortField("time_protonic_verniers", None),
            LEShortField("time_tauron_focusers_perm", None),
            LEShortField("time_regenerative_pau_grids", None),
            LEShortField("time_veteran_damcon_teams", None),
            LEShortField("time_cetrocite_heatsinks", None),
            LEShortField("time_tachyon_scanners", None),
            LEShortField("time_gridscan_overload", None),
            LEShortField("time_override_authorization", None),
            LEShortField("time_resupply_imperatives", None),
            LEShortField("time_patrol_group", None),
            LEShortField("time_fast_supply", None),
            LEShortField("time_vanguard_refit_helm", None),
            LEShortField("time_vanguard_refit_weap", None),
            LEShortField("time_vanguard_refit_comm", None),
            LEShortField("time_vanguard_refit_station", None),
            LEShortField("time_vanguard_refit_eng", None),
            LEShortField("time_vanguard_refit_systems", None),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class Ready(Packet):
    name = "Ready "
    fields_desc = [
        XLEIntField("unknown", 0),
    ]


class RequestEngGridUpdate(Packet):
    name = "RequestEngGridUpdate "
    fields_desc = [
        LEIntField("unknown", 0),
    ]


class SciScan(Packet):
    name = "Science Scan "
    fields_desc = [LEIntField("target_id", 0)]


class SciSelect(Packet):
    name = "Science Select "
    fields_desc = [LEIntField("target_id", 0)]


class ServerHeartbeat(Packet):
    name = "Server Heartbeat "
    fields_desc: Sequence[AnyField] = []


class SetBeamFreq(Packet):
    name = "Set Beam Frequency "
    fields_desc = [LEIntEnumField("beam_frequency", 0, enums.beam_frequency)]


class SetConsole(Packet):
    name = "Set Console "
    fields_desc = [
        LEIntEnumField("console_type", 0, enums.console_type),
        ArtemisSBSBooleanField("selected", False),
    ]


class SetMainScreen(Packet):
    name = "Set Main Screen "
    fields_desc = [LEIntEnumField("main_screen_view", 0, enums.main_screen_view)]


class SetWeaponsTarget(Packet):
    name = "Set Weapons Target "
    fields_desc = [LEIntField("target_id", 1)]


class ShieldsDown(Packet):
    name = "Shields Down "
    fields_desc = [LEIntField("unused", 0)]


class ShieldsUp(Packet):
    name = "Shields Up "
    fields_desc = [LEIntField("unused", 0)]


class SimpleEvent08(Packet):
    name = "Simple Event 08"
    fields_desc = [
        ArtemisSBSFloatField("unknown", 0),
    ]


class SimpleEvent19(Packet):
    name = "Simple Event 19"
    fields_desc = [
        LEIntField("unknown", 0),
    ]


class SingleObjectUpdate(Packet):
    name = "Single Object Update "
    fields_desc = [
        ByteEnumField("object_type", 0, enums.object_type),
        LEIntField("object_id", 0),
    ]


class Skybox(Packet):
    name = "Skybox "
    fields_desc = [
        LEIntField("skybox_id", 0),
    ]


class Smoke(Packet):
    name = "Smoke "
    fields_desc = [
        LEIntField("object_id", 0),
        LEIntField("priority", 0),
        ArtemisSBSFloatField("x", 0),
        ArtemisSBSFloatField("y", 0),
        ArtemisSBSFloatField("z", 0),
    ]


class Tag(Packet):
    name = "Tag "
    fields_desc = [
        LEIntField("object_id", 0),
        LEIntField("unknown", 0),
        ArtemisSBSStrField("tagger", ""),
        ArtemisSBSStrField("date", ""),
    ]


class ToggleAutoBeams(Packet):
    name = "Toggle Auto Beams "
    fields_desc = [LEIntField("unused", 0)]


class TogglePerspective(Packet):
    name = "Toggle Perspective "
    fields_desc = [LEIntField("unused", 0)]


class ToggleRedAlert(Packet):
    name = "Toggle Red Alert "
    fields_desc = [XLEIntField("unused", 0)]


class ToggleShields(Packet):
    name = "Toggle Shields "
    fields_desc = [LEIntField("padding", 0)]


class TorpedoProperties(Packet):
    name = "Torpedo Properties "
    fields_desc = gen_fields(
        [
            ArtemisSBSFloatField("x", None),
            ArtemisSBSFloatField("y", None),
            ArtemisSBSFloatField("z", None),
            ArtemisSBSFloatField("delta_x", None),
            ArtemisSBSFloatField("delta_y", None),
            ArtemisSBSFloatField("delta_z", None),
            LEIntField("unknown_1p7", None),
            LEIntEnumField("ordnance_type", None, enums.ordnance_type),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class UnloadTube(Packet):
    name = "Unload Tube "
    fields_desc = [
        LEIntField("tube_index", 0),
    ]


class Version(Packet):
    name = "Welcome "
    fields_desc = [
        XLEIntField("unknown", 0),
        ArtemisSBSFloatField("version_deprecated", 0),
        VersionField("version", "0.0.0"),
    ]


class WeaponsConsoleProperties(Packet):
    name = "Weapons Console Properties "
    fields_desc = gen_fields(
        [
            ByteField("ordnance_count_1", None),
            ByteField("ordnance_count_2", None),
            ByteField("ordnance_count_3", None),
            ByteField("ordnance_count_4", None),
            ByteField("ordnance_count_5", None),
            ByteField("ordnance_count_6", None),
            ByteField("ordnance_count_7", None),
            ByteField("ordnance_count_8", None),
            ArtemisSBSFloatField("tube_load_time_1", None),
            ArtemisSBSFloatField("tube_load_time_2", None),
            ArtemisSBSFloatField("tube_load_time_3", None),
            ArtemisSBSFloatField("tube_load_time_4", None),
            ArtemisSBSFloatField("tube_load_time_5", None),
            ArtemisSBSFloatField("tube_load_time_6", None),
            ByteEnumField("tube_status_1", None, enums.tube_status),
            ByteEnumField("tube_status_2", None, enums.tube_status),
            ByteEnumField("tube_status_3", None, enums.tube_status),
            ByteEnumField("tube_status_4", None, enums.tube_status),
            ByteEnumField("tube_status_5", None, enums.tube_status),
            ByteEnumField("tube_status_6", None, enums.tube_status),
            ByteEnumField("ordnance_type_1", None, enums.ordnance_type),
            ByteEnumField("ordnance_type_2", None, enums.ordnance_type),
            ByteEnumField("ordnance_type_3", None, enums.ordnance_type),
            ByteEnumField("ordnance_type_4", None, enums.ordnance_type),
            ByteEnumField("ordnance_type_5", None, enums.ordnance_type),
            ByteEnumField("ordnance_type_6", None, enums.ordnance_type),
        ]
    )

    def extract_padding(self, s: bytes) -> Tuple[bytes, Optional[bytes]]:
        return b"", s


class Welcome(Packet):
    name = "Welcome "
    fields_desc = [
        ArtemisSBSStrField("welcome_message", 0),
    ]


def _do_binding(layers):
    for (
        origin,
        internal_type,
        internal_subtype,
    ), type_name in enums.packet_type.items():
        if (layer := layers.get(type_name)) is not None:
            bind_layers(
                ArtemisSBS,
                layer,
                origin=origin,
                internal_type=internal_type,
                internal_subtype=internal_subtype,
            )

    for object_type, object_type_name in enums.object_type.items():
        if (layer := layers.get(object_type_name + "Properties")) is not None:
            bind_layers(SingleObjectUpdate, layer, object_type=object_type)


_do_binding(locals())
