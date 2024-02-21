from scapy.packet import bind_layers as _bind_layers

from ._anomaly_properties import AnomalyProperties
from ._artemissbs_stream import ArtemisSBSStream
from ._artemissbs import ArtemisSBS
from ._asteroid_properties import AsteroidProperties
from ._activate_upgrade import ActivateUpgrade
from ._all_ship_settings import AllShipSettings
from ._base_properties import BaseProperties
from ._beam_fired import BeamFired
from ._black_hole_properties import BlackHoleProperties
from ._captain_select import CaptainSelect
from ._client_heartbeat import ClientHeartbeat
from ._climb_dive import ClimbDive
from ._cloak_decloak import CloakDecloak
from ._comms_incoming import CommsIncoming
from ._comms_outgoing import CommsOutgoing
from ._console_status import ConsoleStatus
from ._creature_properties import CreatureProperties
from ._destroy_object import DestroyObject
from ._detonation import Detonation
from ._docked import Docked
from ._drone_properties import DroneProperties
from ._engineering_console_properties import EngineeringConsoleProperties
from ._eng_grid_update import EngGridUpdate
from ._eng_reset_coolant import EngResetCoolant
from ._eng_send_damcon import EngSendDamcon
from ._eng_set_coolant import EngSetCoolant
from ._eng_set_energy import EngSetEnergy
from ._explosion import Explosion
from ._fighter_bay_status import FighterBayStatus
from ._fire_tube import FireTube
from ._game_master_select_location import GameMasterSelectLocation
from ._game_message import GameMessage
from ._game_start import GameStart
from ._generic_mesh_properties import GenericMeshProperties
from ._helm_jump import HelmJump
from ._helm_request_dock import HelmRequestDock
from ._helm_set_impulse import HelmSetImpulse
from ._helm_set_steering import HelmSetSteering
from ._helm_set_pitch import HelmSetPitch
from ._helm_set_warp import HelmSetWarp
from ._helm_toggle_reverse import HelmToggleReverse
from ._intel import Intel
from ._key_capture_toggle import KeyCaptureToggle
from ._load_tube import LoadTube
from ._mine_properties import MineProperties
from ._nebula_properties import NebulaProperties
from ._npc_ship_properties import NPCShipProperties
from ._object_update import ObjectUpdate
from ._pause import Pause
from ._player_ship_damage import PlayerShipDamage
from ._player_ship_properties import PlayerShipProperties
from ._ready import Ready
from ._request_eng_grid_update import RequestEngGridUpdate
from ._sci_scan import SciScan
from ._sci_select import SciSelect
from ._ship_settings import ShipSettings
from ._server_heartbeat import ServerHeartbeat
from ._set_beam_freq import SetBeamFreq
from ._set_console import SetConsole
from ._set_main_screen import SetMainScreen
from ._set_weapons_target import SetWeaponsTarget
from ._shields_up import ShieldsUp
from ._shields_down import ShieldsDown
from ._single_object_update import SingleObjectUpdate
from ._player_ship_upgrades_properties import PlayerShipUpgradesProperties
from ._simple_event_08 import SimpleEvent08
from ._simple_event_19 import SimpleEvent19
from ._skybox import Skybox
from ._smoke import Smoke
from ._tag import Tag
from ._toggle_auto_beams import ToggleAutoBeams
from ._toggle_perspective import TogglePerspective
from ._toggle_red_alert import ToggleRedAlert
from ._toggle_shields import ToggleShields
from ._torpedo_properties import TorpedoProperties
from ._unload_tube import UnloadTube
from ._version import Version
from ._weapons_console_properties import WeaponsConsoleProperties
from ._welcome import Welcome

from ._binding import do_binding as _do_binding
from .. import enums as _enums

# bind_layers(TCP, ArtemisSBSStream, sport=2010)
# bind_layers(TCP, ArtemisSBSStream, dport=2010)

# bind_layers(ArtemisSBS, Attack, type=0xb83fd2c4)
# bind_layers(ArtemisSBS, CarrierRecord, type=0x9ad1f23b)
# bind_layers(ArtemisSBS, CommText, type=0xd672c35f)
# bind_layers(ArtemisSBS, GMButton, type=0x26faacb9)
# bind_layers(ArtemisSBS, Heartbeat, type=0xf5821226)
# bind_layers(ArtemisSBS, ObjectBitStream, type=0x80803df9)
# bind_layers(ArtemisSBS, ObjectDelete, type=0xcc5a3e30)
# bind_layers(ArtemisSBS, ObjectText, type=0xee665279)
# bind_layers(ArtemisSBS, ShipSystemSync, type=0x077e9f3c)
# bind_layers(ArtemisSBS, SimpleEvent, type=0xf754c8fe)
# bind_layers(ArtemisSBS, ValueFloat, type=0x0351a5ac)
# bind_layers(ArtemisSBS, ValueFourInts, type=0x69cc01d9)
# bind_layers(ArtemisSBS, ValueInt, type=0x4c821d3c)

# bind_layers(Attack, BeamFiredPacket)
# bind_layers(SimpleEvent, CloakDecloakPacket, type=0x07)
# bind_layers(CommText, CommsIncomingPacket)
# bind_layers(ObjectDelete, DestroyObjectPacket)
# bind_layers(ShipSystemSync, EngGridUpdatePacket)
# bind_layers(ValueFourInts, EngResetCoolantPacket, type=0x18)
# bind_layers(ValueFourInts, EngSetCoolantPacket, type=0x00)
# bind_layers(ValueFloat, EngSetEnergyPacket, type=0x04)
# bind_layers(SimpleEvent, ExplosionPacket, type=0x00)
# bind_layers(CarrierRecord, FighterBayStatusPacket)
# bind_layers(ValueInt, FireTubePacket, type=0x08)
# bind_layers(ValueFloat, GameMasterSelectLocationPacket, type=0x06)
# bind_layers(ValueFloat, HelmJumpPacket, type=0x05)
# bind_layers(ValueInt, HelmRequestDockPacket, type=0x07)
# bind_layers(ValueFloat, HelmSetImpulsePacket, type=0x00)
# bind_layers(ValueFloat, HelmSetPitchPacket, type=0x02)
# bind_layers(ValueFloat, HelmSetSteeringPacket, type=0x01)
# bind_layers(ValueInt, HelmSetWarpPacket, type=0x00)
# bind_layers(ObjectText, IntelPacket)
# bind_layers(ObjectBitStream, ObjectUpdatePacket)
# bind_layers(ValueInt, RequestEngGridUpdate, type=0x1a)
# bind_layers(ValueInt, SciScanPacket, type=0x13)
# bind_layers(ValueInt, SciSelectPacket, type=0x10)
# bind_layers(Heartbeat, ServerHeartbeatPacket)
# bind_layers(ValueInt, SetMainScreenPacket, type=0x01)
# bind_layers(ValueInt, SetWeaponsTargetPacket, type=0x02)
# bind_layers(ValueInt, ShieldsDownPacket, type=0x06)
# bind_layers(ValueInt, ShieldsUpPacket, type=0x05)
# bind_layers(ValueInt, ToggleAutoBeamsPacket, type=0x03)
# bind_layers(ValueInt, ToggleRedAlertPacket, type=0x05)
# bind_layers(ValueInt, ToggleShieldsPacket, type=0x04)


_do_binding(_enums.packet_type, locals())


_bind_layers(SingleObjectUpdate, PlayerShipProperties, object_type=0x01)
_bind_layers(SingleObjectUpdate, WeaponsConsoleProperties, object_type=0x02)
_bind_layers(SingleObjectUpdate, EngineeringConsoleProperties, object_type=0x03)
_bind_layers(SingleObjectUpdate, PlayerShipUpgradesProperties, object_type=0x04)
_bind_layers(SingleObjectUpdate, NPCShipProperties, object_type=0x05)
_bind_layers(SingleObjectUpdate, BaseProperties, object_type=0x06)
_bind_layers(SingleObjectUpdate, MineProperties, object_type=0x07)
_bind_layers(SingleObjectUpdate, AnomalyProperties, object_type=0x08)
_bind_layers(SingleObjectUpdate, NebulaProperties, object_type=0x0A)
_bind_layers(SingleObjectUpdate, TorpedoProperties, object_type=0x0B)
_bind_layers(SingleObjectUpdate, BlackHoleProperties, object_type=0x0C)
_bind_layers(SingleObjectUpdate, AsteroidProperties, object_type=0x0D)
_bind_layers(SingleObjectUpdate, GenericMeshProperties, object_type=0x0E)
_bind_layers(SingleObjectUpdate, CreatureProperties, object_type=0x0F)
_bind_layers(SingleObjectUpdate, DroneProperties, object_type=0x10)
