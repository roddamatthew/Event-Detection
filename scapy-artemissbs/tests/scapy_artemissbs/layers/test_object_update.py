import pytest
from scapy.all import Raw

from scapy_artemissbs.layers import (
    AnomalyProperties,
    BaseProperties,
    BlackHoleProperties,
    CreatureProperties,
    EngineeringConsoleProperties,
    NebulaProperties,
    NPCShipProperties,
    ObjectUpdate,
    PlayerShipProperties,
    PlayerShipUpgradesProperties,
    SingleObjectUpdate,
    TorpedoProperties,
)

examples = [
    (
        b"\x03\xbc\x07\x00\x00\xf7\x00\x00\x00\xa7\x7fB:\xa7\x7fB:\xa7\x7fB:\xa7\x7fB:\xa7\x7fB:\xa7\x7fB:\xa7\x7fB:\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type="EngineeringConsole", object_id=1980)
                / EngineeringConsoleProperties(
                    flags=4143972352,
                    heat_level_1=0.0007419534376822412,
                    heat_level_2=0.0007419534376822412,
                    heat_level_3=0.0007419534376822412,
                    heat_level_5=0.0007419534376822412,
                    heat_level_6=0.0007419534376822412,
                    heat_level_7=0.0007419534376822412,
                    heat_level_8=0.0007419534376822412,
                )
            ],
            padding=0,
        ),
    ),
    (
        b"\x01\xee\x03\x00\x00\x80(\x01\x00\x00\x00\xdblkDr\xf3.G\xef\x16\x0fG\xc0\xcdE\xc0\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type="PlayerShip", object_id=1006)
                / PlayerShipProperties(
                    flags=140909303824384,
                    energy_reserves=941.7008666992188,
                    x=44787.4453125,
                    z=36630.93359375,
                    heading=-3.0906829833984375,
                )
            ],
            padding=0,
        ),
    ),
    (
        b"\x06\xed\x03\x00\x00\x02\x00j\x05\xc7C\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type="Base", object_id=1005)
                / BaseProperties(flags=["shields"], shields=398.04229736328125)
            ],
            padding=0,
        ),
    ),
    (
        b"\x01\xee\x03\x00\x00\x80(\x01\x00\x00\x00\xdblkDr\xf3.G\xef\x16\x0fG\xc0\xcdE\xc0\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=1, object_id=1006)
                / PlayerShipProperties(
                    flags=140909303824384,
                    energy_reserves=941.7008666992188,
                    x=44787.4453125,
                    z=36630.93359375,
                    heading=-3.0906829833984375,
                )
            ],
            padding=0,
        ),
    ),
    (
        b"\x01\xee\x03\x00\x00\x80(\x01\x00\x00\x00\xe7hkDA\xf3.G\x93\x10\x0fG\x88DH\xc0\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=1, object_id=1006)
                / PlayerShipProperties(
                    flags=140909303824384,
                    energy_reserves=941.6390991210938,
                    x=44787.25390625,
                    z=36624.57421875,
                    heading=-3.129182815551758,
                )
            ],
            padding=0,
        ),
    ),
    (
        b"\x01\xee\x03\x00\x00\xff\xff\xff\xff\xff\x1f\x00\x00\x00\x00\xa0\xc2\xf5>\x00\x00\x00\x00\x9a\x99\x19?o\x12\x83;\x01\x00k=kD\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01/G\x1a\xe1\xa4\xc2\xbd\xcc\x0eG\x00\x00\x00\x00\x90\x07,>\x96\xc0.@\xc7t\x93>\x00\x08\x00\x00\x00A\x00r\x00t\x00e\x00m\x00i\x00s\x00\x00\x00\x00\x00\xa0B\x00\x00\xa0B\x00\x00\xa0B\x00\x00\xa0B\x00\x00\x00\x00\x00\x00PCH\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Q\x00\x00\x00\x00\x00\x00\x02\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=1, object_id=1006)
                / PlayerShipProperties(
                    flags=281474976710431,
                    weapons_target=0,
                    impulse=0.48000049591064453,
                    rudder=0.0,
                    top_speed=0.6000000238418579,
                    turn_rate=0.004000000189989805,
                    auto_beams=True,
                    warp_factor=0,
                    energy_reserves=940.9596557617188,
                    shields_up_or_down=True,
                    unknown_2p2=1,
                    hull_id=0,
                    x=44801.0,
                    y=-82.43965148925781,
                    z=36556.73828125,
                    pitch=0.0,
                    roll=0.1679975986480713,
                    heading=2.7305045127868652,
                    velocity=0.28800031542778015,
                    nebula_type=0,
                    ship_name="Artemis",
                    forward_shields=80.0,
                    forward_shields_max=80.0,
                    aft_shields=80.0,
                    aft_shields_max=80.0,
                    last_docked_base=0,
                    alert_status=0,
                    unknown_4p3=200000.0,
                    main_screen_view=0,
                    beam_frequency=0,
                    available_coolant_or_missiles=8,
                    science_target=0,
                    captain_target=0,
                    drive_type=0,
                    scanning_id=0,
                    scanning_progress=7.438675188797288e-39,
                    reverse=False,
                    climb_or_dive=0.0,
                    side=2,
                    map_visibility=4294967295,
                    ship_index=0,
                    capital_ship_object_id=0,
                    accent_color=0.0,
                    emergency_jump_cooldown=0.0,
                    beacon_creature_type=0,
                    beacon_mode=0,
                )
            ],
            padding=0,
        ),
    ),
    (
        b"\x06\xe8\x03\x00\x00\xff?\x04\x00\x00\x00D\x00S\x001\x00\x00\x00\x00\x00\xc8C\x00\x00\xc8C\x06\x00\x00\x00\xe8\x03\x00\x00\xbaADG\x00\x00\x00\x00\xc7\x8fCG\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x06\xe9\x03\x00\x00\xff?\x04\x00\x00\x00D\x00S\x002\x00\x00\x00\x00\x00\xc8C\x00\x00\xc8C\x06\x00\x00\x00\xe8\x03\x00\x00P\x076G\x00\x00\x00\x00\xe2O\x13G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x06\xea\x03\x00\x00\xff?\x04\x00\x00\x00D\x00S\x003\x00\x00\x00\x00\x00\xc8C\x00\x00\xc8C\x06\x00\x00\x00\xe8\x03\x00\x00\x16\xcb\x07G\x00\x00\x00\x00\x9d\x03`G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x06\xeb\x03\x00\x00\xff?\x04\x00\x00\x00D\x00S\x004\x00\x00\x00\x00\x00\xc8C\x00\x00\xc8C\x06\x00\x00\x00\xe8\x03\x00\x00&r\xf7F\x00\x00\x00\x00^\xe4VG\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x06\xec\x03\x00\x00\xff?\x04\x00\x00\x00D\x00S\x005\x00\x00\x00\x00\x00\xc8C\x00\x00\xc8C\x06\x00\x00\x00\xe8\x03\x00\x00\xc4\xa9\x0cG\x00\x00\x00\x007\x80|G\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=6, object_id=1000)
                / BaseProperties(
                    flags=[
                        "unknown_2p1",
                        "unknown_2p2",
                        "unknown_2p3",
                        "unknown_2p4",
                        "unknown_2p5",
                        "side",
                        "name_",
                        "shields",
                        "max_shields",
                        "unknown_1p4",
                        "hull_id",
                        "x",
                        "y",
                        "z",
                    ],
                    name_="DS1",
                    shields=400.0,
                    max_shields=400.0,
                    unknown_1p4=6,
                    hull_id=1000,
                    x=50241.7265625,
                    y=0.0,
                    z=50063.77734375,
                    unknown_2p1=0,
                    unknown_2p2=0,
                    unknown_2p3=0,
                    unknown_2p4=0,
                    unknown_2p5=0,
                    side=2,
                ),
                SingleObjectUpdate(object_type=6, object_id=1001)
                / BaseProperties(
                    flags=[
                        "unknown_2p1",
                        "unknown_2p2",
                        "unknown_2p3",
                        "unknown_2p4",
                        "unknown_2p5",
                        "side",
                        "name_",
                        "shields",
                        "max_shields",
                        "unknown_1p4",
                        "hull_id",
                        "x",
                        "y",
                        "z",
                    ],
                    name_="DS2",
                    shields=400.0,
                    max_shields=400.0,
                    unknown_1p4=6,
                    hull_id=1000,
                    x=46599.3125,
                    y=0.0,
                    z=37711.8828125,
                    unknown_2p1=0,
                    unknown_2p2=0,
                    unknown_2p3=0,
                    unknown_2p4=0,
                    unknown_2p5=0,
                    side=2,
                ),
                SingleObjectUpdate(object_type=6, object_id=1002)
                / BaseProperties(
                    flags=[
                        "unknown_2p1",
                        "unknown_2p2",
                        "unknown_2p3",
                        "unknown_2p4",
                        "unknown_2p5",
                        "side",
                        "name_",
                        "shields",
                        "max_shields",
                        "unknown_1p4",
                        "hull_id",
                        "x",
                        "y",
                        "z",
                    ],
                    name_="DS3",
                    shields=400.0,
                    max_shields=400.0,
                    unknown_1p4=6,
                    hull_id=1000,
                    x=34763.0859375,
                    y=0.0,
                    z=57347.61328125,
                    unknown_2p1=0,
                    unknown_2p2=0,
                    unknown_2p3=0,
                    unknown_2p4=0,
                    unknown_2p5=0,
                    side=2,
                ),
                SingleObjectUpdate(object_type=6, object_id=1003)
                / BaseProperties(
                    flags=[
                        "unknown_2p1",
                        "unknown_2p2",
                        "unknown_2p3",
                        "unknown_2p4",
                        "unknown_2p5",
                        "side",
                        "name_",
                        "shields",
                        "max_shields",
                        "unknown_1p4",
                        "hull_id",
                        "x",
                        "y",
                        "z",
                    ],
                    name_="DS4",
                    shields=400.0,
                    max_shields=400.0,
                    unknown_1p4=6,
                    hull_id=1000,
                    x=31673.07421875,
                    y=0.0,
                    z=55012.3671875,
                    unknown_2p1=0,
                    unknown_2p2=0,
                    unknown_2p3=0,
                    unknown_2p4=0,
                    unknown_2p5=0,
                    side=2,
                ),
                SingleObjectUpdate(object_type=6, object_id=1004)
                / BaseProperties(
                    flags=[
                        "unknown_2p1",
                        "unknown_2p2",
                        "unknown_2p3",
                        "unknown_2p4",
                        "unknown_2p5",
                        "side",
                        "name_",
                        "shields",
                        "max_shields",
                        "unknown_1p4",
                        "hull_id",
                        "x",
                        "y",
                        "z",
                    ],
                    name_="DS5",
                    shields=400.0,
                    max_shields=400.0,
                    unknown_1p4=6,
                    hull_id=1000,
                    x=36009.765625,
                    y=0.0,
                    z=64640.21484375,
                    unknown_2p1=0,
                    unknown_2p2=0,
                    unknown_2p3=0,
                    unknown_2p4=0,
                    unknown_2p5=0,
                    side=2,
                ),
            ],
            padding=0,
        ),
    ),
    (
        b"\x0f\xb2\x07\x00\x00'\x00\x00\xa8\xectG\xbd\x9cjAmz\x1aG1Y\xa8\xae\x0f\xb3\x07\x00\x00'\x00\x00\xd0AuGK\xb3jA\x08\x95\x1bG\xab1w\xae\x0f\xb6\x07\x00\x00'\x00\x00\x14ytG\n\x85jA6\x95\x1aG+\xa7\xce\xae\x0f\xb7\x07\x00\x00'\x00\x00\x06\xc5tG\x83\x96jA<\xd6\x1aG\x9d\xd1\xad\xae\x0f\xb8\x07\x00\x00\x05\x00\x00L\x83\xeeE\xd3\xe2\xfaF\x0f\x7f\t\x00\x00P\x00\x00Z\x99\xde?\xc18,C\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=15, object_id=1970)
                / CreatureProperties(
                    flags=["x", "y", "z", "pitch"],
                    x=62700.65625,
                    y=14.6632661819458,
                    z=39546.42578125,
                    pitch=-7.655599071343389e-11,
                ),
                SingleObjectUpdate(object_type=15, object_id=1971)
                / CreatureProperties(
                    flags=["x", "y", "z", "pitch"],
                    x=62785.8125,
                    y=14.66877269744873,
                    z=39829.03125,
                    pitch=-5.620541185247241e-11,
                ),
                SingleObjectUpdate(object_type=15, object_id=1974)
                / CreatureProperties(
                    flags=["x", "y", "z", "pitch"],
                    x=62585.078125,
                    y=14.657480239868164,
                    z=39573.2109375,
                    pitch=-9.397490424722932e-11,
                ),
                SingleObjectUpdate(object_type=15, object_id=1975)
                / CreatureProperties(
                    flags=["x", "y", "z", "pitch"],
                    x=62661.0234375,
                    y=14.66174602508545,
                    z=39638.234375,
                    pitch=-7.904363968913586e-11,
                ),
                SingleObjectUpdate(object_type=15, object_id=1976)
                / CreatureProperties(
                    flags=["x", "z"],
                    x=7632.412109375,
                    z=32113.412109375,
                ),
                SingleObjectUpdate(object_type=15, object_id=2431)
                / CreatureProperties(
                    flags=["heading", "roll"],
                    heading=1.7390549182891846,
                    roll=172.22169494628906,
                ),
            ],
            padding=0,
        ),
    ),
    (
        b"\x04\xbc\x07\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=4, object_id=1980)
                / PlayerShipUpgradesProperties(
                    flags=[
                        "time_vanguard_refit_comm",
                        "time_vanguard_refit_station",
                        "time_vanguard_refit_eng",
                        "time_vanguard_refit_systems",
                        "time_tachyon_scanners",
                        "time_gridscan_overload",
                        "time_override_authorization",
                        "time_resupply_imperatives",
                        "time_patrol_group",
                        "time_fast_supply",
                        "time_vanguard_refit_helm",
                        "time_vanguard_refit_weap",
                        "time_double_agent",
                        "time_wartime_production",
                        "time_infusion_p_coils_perm",
                        "time_protonic_verniers",
                        "time_tauron_focusers_perm",
                        "time_regenerative_pau_grids",
                        "time_veteran_damcon_teams",
                        "time_cetrocite_heatsinks",
                        "time_infusion_p_coils",
                        "time_hydrogen_ram",
                        "time_tauron_focusers",
                        "time_carapaction_coils",
                        "time_polyphasic_capacitors",
                        "time_cetrocite_crystals",
                        "time_lateral_array",
                        "time_ecm_starpulse",
                        "count_patrol_group",
                        "count_fast_supply",
                        "count_vanguard_refit_helm",
                        "count_vanguard_refit_weap",
                        "count_vanguard_refit_comm",
                        "count_vanguard_refit_station",
                        "count_vanguard_refit_eng",
                        "count_vanguard_refit_systems",
                        "count_tauron_focusers_perm",
                        "count_regenerative_pau_grids",
                        "count_veteran_damcon_teams",
                        "count_cetrocite_heatsinks",
                        "count_tachyon_scanners",
                        "count_gridscan_overload",
                        "count_override_authorization",
                        "count_resupply_imperatives",
                        "count_polyphasic_capacitors",
                        "count_cetrocite_crystals",
                        "count_lateral_array",
                        "count_ecm_starpulse",
                        "count_double_agent",
                        "count_wartime_production",
                        "count_infusion_p_coils_perm",
                        "count_protonic_verniers",
                        "active_vanguard_refit_comm",
                        "active_vanguard_refit_station",
                        "active_vanguard_refit_eng",
                        "active_vanguard_refit_systems",
                        "count_infusion_p_coils",
                        "count_hydrogen_ram",
                        "count_tauron_focusers",
                        "count_carapaction_coils",
                        "active_tachyon_scanners",
                        "active_gridscan_overload",
                        "active_override_authorization",
                        "active_resupply_imperatives",
                        "active_patrol_group",
                        "active_fast_supply",
                        "active_vanguard_refit_helm",
                        "active_vanguard_refit_weap",
                        "active_double_agent",
                        "active_wartime_production",
                        "active_infusion_p_coils_perm",
                        "active_protonic_verniers",
                        "active_tauron_focusers_perm",
                        "active_regenerative_pau_grids",
                        "active_veteran_damcon_teams",
                        "active_cetrocite_heatsinks",
                        "active_infusion_p_coils",
                        "active_hydrogen_ram",
                        "active_tauron_focusers",
                        "active_carapaction_coils",
                        "active_polyphasic_capacitors",
                        "active_cetrocite_crystals",
                        "active_lateral_array",
                        "active_ecm_starpulse",
                    ],
                    active_infusion_p_coils=False,
                    active_hydrogen_ram=False,
                    active_tauron_focusers=False,
                    active_carapaction_coils=False,
                    active_polyphasic_capacitors=False,
                    active_cetrocite_crystals=False,
                    active_lateral_array=False,
                    active_ecm_starpulse=False,
                    active_double_agent=False,
                    active_wartime_production=False,
                    active_infusion_p_coils_perm=False,
                    active_protonic_verniers=False,
                    active_tauron_focusers_perm=False,
                    active_regenerative_pau_grids=False,
                    active_veteran_damcon_teams=False,
                    active_cetrocite_heatsinks=False,
                    active_tachyon_scanners=False,
                    active_gridscan_overload=False,
                    active_override_authorization=False,
                    active_resupply_imperatives=False,
                    active_patrol_group=False,
                    active_fast_supply=False,
                    active_vanguard_refit_helm=False,
                    active_vanguard_refit_weap=False,
                    active_vanguard_refit_comm=False,
                    active_vanguard_refit_station=False,
                    active_vanguard_refit_eng=False,
                    active_vanguard_refit_systems=False,
                    count_infusion_p_coils=1,
                    count_hydrogen_ram=0,
                    count_tauron_focusers=1,
                    count_carapaction_coils=0,
                    count_polyphasic_capacitors=0,
                    count_cetrocite_crystals=0,
                    count_lateral_array=0,
                    count_ecm_starpulse=0,
                    count_double_agent=0,
                    count_wartime_production=0,
                    count_infusion_p_coils_perm=0,
                    count_protonic_verniers=0,
                    count_tauron_focusers_perm=0,
                    count_regenerative_pau_grids=0,
                    count_veteran_damcon_teams=0,
                    count_cetrocite_heatsinks=0,
                    count_tachyon_scanners=0,
                    count_gridscan_overload=0,
                    count_override_authorization=0,
                    count_resupply_imperatives=0,
                    count_patrol_group=0,
                    count_fast_supply=0,
                    count_vanguard_refit_helm=0,
                    count_vanguard_refit_weap=0,
                    count_vanguard_refit_comm=0,
                    count_vanguard_refit_station=0,
                    count_vanguard_refit_eng=0,
                    count_vanguard_refit_systems=0,
                    time_infusion_p_coils=0,
                    time_hydrogen_ram=0,
                    time_tauron_focusers=0,
                    time_carapaction_coils=0,
                    time_polyphasic_capacitors=0,
                    time_cetrocite_crystals=0,
                    time_lateral_array=0,
                    time_ecm_starpulse=0,
                    time_double_agent=0,
                    time_wartime_production=0,
                    time_infusion_p_coils_perm=0,
                    time_protonic_verniers=0,
                    time_tauron_focusers_perm=0,
                    time_regenerative_pau_grids=0,
                    time_veteran_damcon_teams=0,
                    time_cetrocite_heatsinks=0,
                    time_tachyon_scanners=0,
                    time_gridscan_overload=0,
                    time_override_authorization=0,
                    time_resupply_imperatives=0,
                    time_patrol_group=0,
                    time_fast_supply=0,
                    time_vanguard_refit_helm=0,
                    time_vanguard_refit_weap=0,
                    time_vanguard_refit_comm=0,
                    time_vanguard_refit_station=0,
                    time_vanguard_refit_eng=0,
                    time_vanguard_refit_systems=0,
                )
            ],
            padding=0,
        ),
    ),
    (
        b"\x0bA\x0b\x00\x00\xff\x00\xb0\x81RGb\xd4\x07B\xf2|CG\xd7\xf2b?\xa8\x8b\xec>\xb5\x19\xcf<\x0b\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=11, object_id=2881)
                / TorpedoProperties(
                    flags=[
                        "x",
                        "y",
                        "z",
                        "delta_x",
                        "delta_y",
                        "delta_z",
                        "unknown_1p7",
                        "ordnance_type",
                    ],
                    x=53889.6875,
                    y=33.95740509033203,
                    z=50044.9453125,
                    delta_x=0.8865179419517517,
                    delta_y=0.4620029926300049,
                    delta_z=0.02528081275522709,
                    unknown_1p7=11,
                    ordnance_type=3,
                )
            ],
            padding=0,
        ),
    ),
    (
        b"\x0c\x93\x07\x00\x00\x07D\xb7dG\x00\x00\x00\x00,\x83\x19G\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=12, object_id=1939)
                / BlackHoleProperties(
                    flags=["x", "y", "z"], x=58551.265625, y=0.0, z=39299.171875
                )
            ],
            padding=0,
        ),
    ),
    (
        b"\n\x98\x07\x00\x00\x7f\xfc%\x93G\x00\x00\x00\x00\xe8\\\x85G\xcd\xcc\xcc>\x00\x00\x00\x00\x8d%?>\x02\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=10, object_id=1944)
                / NebulaProperties(
                    flags=[
                        "x",
                        "y",
                        "z",
                        "red_color_channel",
                        "green_color_channel",
                        "blue_color_channel",
                        "type",
                    ],
                    x=75339.96875,
                    y=0.0,
                    z=68281.8125,
                    red_color_channel=0.4000000059604645,
                    green_color_channel=0.0,
                    blue_color_channel=0.18666668236255646,
                    type=2,
                )
            ],
            padding=0,
        ),
    ),
    (
        b"\n\x9b\x07\x00\x00\x7f\xa8\xe9\x97G\x00\x00\x00\x00@\xd5\x87G\xcd\xcc\xcc>\x00\x00\x00\x00\xcd/\x16>\x02\n\xad\x07\x00\x00\x7f}\xb5zG\x00\x00\x00\x00\xb4\x89\x9fF\xcd\xcc\xcc>\x00\x00\x00\x00\x9a%?=\x02\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=10, object_id=1947)
                / NebulaProperties(
                    flags="x+y+z+red_color_channel+green_color_channel+blue_color_channel+type",
                    x=77779.3125,
                    y=0.0,
                    z=69546.5,
                    red_color_channel=0.4000000059604645,
                    green_color_channel=0.0,
                    blue_color_channel=0.1466667205095291,
                    type=2,
                ),
                SingleObjectUpdate(object_type=10, object_id=1965)
                / NebulaProperties(
                    flags="x+y+z+red_color_channel+green_color_channel+blue_color_channel+type",
                    x=64181.48828125,
                    y=0.0,
                    z=20420.8515625,
                    red_color_channel=0.4000000059604645,
                    green_color_channel=0.0,
                    blue_color_channel=0.046666719019412994,
                    type=2,
                ),
            ],
            padding=0,
        ),
    ),
    (
        b"\x05\xf7\x08\x00\x00\x00\t\x00\x00\x00\x00\x00(/\x89\xc3\x86\x01\x00\x80\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=5, object_id=2295)
                / NPCShipProperties(
                    flags="y+roll",
                    y=-274.368408203125,
                    roll=-5.4650640108667866e-43,
                )
            ],
            padding=0,
        ),
    ),
    (
        b"\x05\x04\t\x00\x00\x84\x1b\x00\x00\x00\x00\x00\xdc%\xdf>\x90\xed\xf0F\xcd\x8a\xae\xc2\xd5\xde\x96G\tu\xf0=.y\xf0?\x00\x00\x00\x00",
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=5, object_id=2308)
                / NPCShipProperties(
                    flags=37184383739756544,
                    rudder=0.43583571910858154,
                    x=30838.78125,
                    y=-87.2710952758789,
                    z=77245.6640625,
                    roll=0.11741072684526443,
                    heading=1.8786981105804443,
                )
            ],
            padding=0,
        ),
    ),
    (
        bytes.fromhex(
            "08b2060000ff001e069b47000000000bde6a47010000000000000000000000000008b3060000ff00ff6275470000000097b9c946020000000000000000000000000000000000"
        ),
        ObjectUpdate(
            updates=[
                SingleObjectUpdate(object_type=8, object_id=1714)
                / AnomalyProperties(
                    flags=[
                        "x",
                        "y",
                        "z",
                        "anomaly_type",
                        "scan",
                        "unknown",
                        "creature_type",
                        "beacon_mode",
                    ],
                    x=79372.234375,
                    y=0.0,
                    z=60126.04296875,
                    anomaly_type=1,
                    scan=0,
                    unknown=0,
                    creature_type=0,
                    beacon_mode=0,
                ),
                SingleObjectUpdate(object_type=8, object_id=1715)
                / AnomalyProperties(
                    flags=[
                        "x",
                        "y",
                        "z",
                        "anomaly_type",
                        "scan",
                        "unknown",
                        "creature_type",
                        "beacon_mode",
                    ],
                    x=62818.99609375,
                    y=0.0,
                    z=25820.794921875,
                    anomaly_type=2,
                    scan=0,
                    unknown=0,
                    creature_type=0,
                    beacon_mode=0,
                ),
            ],
            padding=0,
        ),
    ),
]


class TestInit:
    @pytest.mark.parametrize("bytes_, packet", examples)
    def test_dissect(self, bytes_, packet):
        assert ObjectUpdate(bytes_) == packet

    @pytest.mark.parametrize("bytes_, packet", examples)
    def test_build(self, bytes_, packet):
        packet = packet.copy()
        for sou in packet.updates:
            sou[1].flags = None
        assert bytes(packet) == bytes_

    @pytest.mark.parametrize(
        "bytes_",
        [
            # b"\x06\xbb\x07\x00\x00\x02\x00\xa3p\xabC",
            b"\x05\xf7\x08\x00\x00\x00\t\x00\x00\x00\x00\x00(/\x89\xc3\x86\x01\x00\x80\x00",
            b"\x05\x04\t\x00\x00\x84\x1b\x00\x00\x00\x00\x00\xdc%\xdf>\x90\xed\xf0F\xcd\x8a\xae\xc2\xd5\xde\x96G\tu\xf0=.y\xf0?\x00\x00\x00",
        ],
    )
    def test_malformed(self, bytes_):
        with pytest.raises(Exception):
            print(repr(ObjectUpdate(bytes_)))
