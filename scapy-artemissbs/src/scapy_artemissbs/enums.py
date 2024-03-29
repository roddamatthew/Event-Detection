alert_status = {
    0x00: "normal",
    0x01: "red alert",
}

anomaly_type = {
    0x00: "HiDens Power Cell",
    0x01: "Vigoranium Nodule",
    0x02: "Cetrocite Crystal",
    0x03: "Lateral Array",
    0x04: "Tauron Focusers",
    0x05: "Infusion P-Coils",
    0x06: "Carapaction Coils",
    0x07: "Secret code case",
    0x08: "Beacon",
    0x09: "Space junk",
}

beacon_mode = {
    0x00: "attract",
    0x01: "repel",
}

beam_frequency = {
    0x00: "A",
    0x01: "B",
    0x02: "C",
    0x03: "D",
    0x04: "E",
}

drive_type = {
    0x00: "warp",
    0x01: "jump",
}

comm_target_type = {
    0x00: "player",
    0x01: "enemy ship",
    0x02: "station",
    0x03: "other",
}

console_status = {
    0x00: "available",
    0x01: "yours",
    0x02: "unavailable",
}

console_type = {
    0x00: "main screen",
    0x01: "helm",
    0x02: "weapons",
    0x03: "engineering",
    0x04: "science",
    0x05: "communications",
    0x06: "single-seat craft",
    0x07: "data",
    0x08: "observer",
    0x09: "captain's map",
    0x0A: "game master",
}

creature_type = {
    0x00: "typhon",
    0x01: "whale",
    0x02: "shark",
    0x03: "dragon",
    0x04: "piranha",
    0x05: "charybdis",
    0x06: "insect",
    0x07: "jelly",
    0x08: "wreck",
}

game_type = {
    0x00: "siege",
    0x01: "single front",
    0x02: "double front",
    0x03: "deep strike",
    0x04: "peacetime",
    0x05: "border war",
    0x06: "infestation",
}

intel_type = {
    0x00: "race",
    0x01: "class",
    0x02: "level 1 scan description",
    0x03: "level 2 scan description",
}

internal_type = {
    0x0351A5AC: "valueFloat",
    0x4C821D3C: "valueInt",
    0x574C4C4B: "commsMessage",
    0x69CC01D9: "valueFourInts",
    0x6AADC57F: "controlMessage",
    0x809305A7: "gmText",
    0xC2BEE72E: "beamRequest",
    0x077E9F3C: "shipSystemSync",
    0x19C6E2D4: "clientConsoles",
    0x26FAACB9: "gmButton",
    0x3DE66711: "startGame",
    0x6D04B3DA: "plainTextGreeting",
    0x80803DF9: "objectBitStream",
    0x902F0B1A: "bigMess",
    0x9AD1F23B: "carrierRecord",
    0xAE88E058: "incomingMessage",
    0xB83FD2C4: "attack",
    0xBE991309: "idleText",
    0xCA88F050: "commsButton",
    0xCC5A3E30: "objectDelete",
    0xD672C35F: "commText",
    0xE548E74A: "connected",
    0xEE665279: "objectText",
    0xF5821226: "heartbeat",
    0xF754C8FE: "simpleEvent",
}

main_screen_view = {
    0x00: "forward",
    0x01: "port",
    0x02: "starboard",
    0x03: "aft",
    0x04: "tactical",
    0x05: "long range",
    0x06: "status",
}

object_type = {
    0x00: "End",
    0x01: "PlayerShip",
    0x02: "WeaponsConsole",
    0x03: "EngineeringConsole",
    0x04: "PlayerShipUpgrades",
    0x05: "NPCShip",
    0x06: "Base",
    0x07: "Mine",
    0x08: "Anomaly",
    0x09: "Unused",
    0x0A: "Nebula",
    0x0B: "Torpedo",
    0x0C: "BlackHole",
    0x0D: "Asteroid",
    0x0E: "GenericMesh",
    0x0F: "Creature",
    0x10: "Drone",
}

ordnance_type = {
    0x00: "homing missile",
    0x01: "nuke",
    0x02: "mine",
    0x03: "EMP",
    0x04: "plasma shock",
    0x05: "beacon",
    0x06: "probe",
    0x07: "tag",
}

ship_system = {
    0x00: "beams",
    0x01: "torpedoes",
    0x02: "sensors",
    0x03: "maneuvering",
    0x04: "impulse",
    0x05: "warp/jump drive",
    0x06: "fore shields",
    0x07: "aft shields",
}

targeting_mode = {
    0x00: "auto",
    0x01: "manual",
}

tube_status = {
    0x00: "unloaded",
    0x01: "loaded",
    0x02: "loading",
    0x03: "unloading",
}

upgrades = {
    0x00: "Infusion P-Coils",
    0x01: "Hydrogen Ram",
    0x02: "Tauron Focusers",
    0x03: "Carapction Coils",
    0x04: "Polyphasic Capacitors",
    0x05: "Coolant Reserves",
    0x06: "Lateral Array",
    0x07: "ECM Starpulse",
    0x08: "Double Agent",
    0x09: "Wartime Production",
    0x0A: "Infusion P-Coils PERM",
    0x0B: "Protonic Verniers",
    0x0C: "Tauron Focusers PERM",
    0x0D: "Regenerative Pau-Grids",
    0x0E: "Veteran DamCon Teams",
    0x0F: "Cetrocite Heatsinks",
    0x10: "Tachyon Scanners",
    0x11: "Gridscan Overload",
    0x12: "Override Authorization",
    0x13: "Resupply Imperatives",
    0x14: "Patrol Group",
    0x15: "Fast Supply",
    0x16: "Vanguard Refit",
    0x17: "Vanguard Refit",
    0x18: "Vanguard Refit",
    0x19: "Vanguard Refit",
    0x1A: "Vanguard Refit",
    0x1B: "Vanguard Refit",
}


packet_type = {
    (2, 0x0351A5AC, 0x00): "HelmSetImpulse",
    (2, 0x0351A5AC, 0x01): "HelmSetSteering",
    (2, 0x0351A5AC, 0x02): "HelmSetPitch",
    (2, 0x0351A5AC, 0x03): "ValueFloat03",
    (2, 0x0351A5AC, 0x04): "EngSetEnergy",
    (2, 0x0351A5AC, 0x05): "HelmJump",
    (2, 0x0351A5AC, 0x06): "GameMasterSelectLocation",
    (2, 0x0351A5AC, 0x07): "FighterPilot",
    (1, 0x077E9F3C, 0x00): "EngGridUpdate",
    (1, 0x19C6E2D4, 0x00): "ConsoleStatus",
    (1, 0x26FAACB9, 0x00): "RemoveGMButton",
    (1, 0x26FAACB9, 0x01): "AddGMButton",
    (1, 0x26FAACB9, 0x02): "AddGMButtonAtPosition",
    (1, 0x26FAACB9, 0x03): "SetDefaultGMButtonWidth",
    (1, 0x26FAACB9, 0x63): "GameMasterInstructions",
    (1, 0x26FAACB9, 0x64): "RemoveAllGMButtons",
    (1, 0x3DE66711, 0x00): "GameStart",
    (2, 0x4C821D3C, 0x00): "HelmSetWarp",
    (2, 0x4C821D3C, 0x01): "SetMainScreen",
    (2, 0x4C821D3C, 0x02): "SetWeaponsTarget",
    (2, 0x4C821D3C, 0x03): "ToggleAutoBeams",
    (2, 0x4C821D3C, 0x04): "ToggleShields",
    (2, 0x4C821D3C, 0x05): "ShieldsUp",
    (2, 0x4C821D3C, 0x06): "ShieldsDown",
    (2, 0x4C821D3C, 0x07): "HelmRequestDock",
    (2, 0x4C821D3C, 0x08): "FireTube",
    (2, 0x4C821D3C, 0x09): "UnloadTube",
    (2, 0x4C821D3C, 0x0A): "ToggleRedAlert",
    (2, 0x4C821D3C, 0x0B): "SetBeamFreq",
    (2, 0x4C821D3C, 0x0C): "EngSetAutoDamcon",
    (2, 0x4C821D3C, 0x0D): "SetShip",
    (2, 0x4C821D3C, 0x0E): "SetConsole",
    (2, 0x4C821D3C, 0x0F): "Ready",
    (2, 0x4C821D3C, 0x10): "SciSelect",
    (2, 0x4C821D3C, 0x11): "CaptainSelect",
    (2, 0x4C821D3C, 0x12): "GameMasterSelectObject",
    (2, 0x4C821D3C, 0x13): "SciScan",
    (2, 0x4C821D3C, 0x14): "Keystroke",
    (2, 0x4C821D3C, 0x15): "ButtonClick",
    (2, 0x4C821D3C, 0x16): "ValueInt16",
    (2, 0x4C821D3C, 0x17): "SetShipSettings",
    (2, 0x4C821D3C, 0x18): "EngResetCoolant",
    (2, 0x4C821D3C, 0x19): "HelmToggleReverse",
    (2, 0x4C821D3C, 0x1A): "RequestEngGridUpdate",
    (2, 0x4C821D3C, 0x1B): "TogglePerspective",
    (2, 0x4C821D3C, 0x1C): "ActivateUpgrade",
    (2, 0x4C821D3C, 0x1D): "ClimbDive",
    (2, 0x4C821D3C, 0x1E): "FighterLaunch",
    (2, 0x4C821D3C, 0x1F): "FighterShoot",
    (2, 0x4C821D3C, 0x20): "EmergencyJump",
    (2, 0x4C821D3C, 0x21): "SetFighterSettings",
    (2, 0x4C821D3C, 0x22): "BeaconConfig",
    (2, 0x4C821D3C, 0x24): "ClientHeartbeat",
    (2, 0x574C4C4B, 0x00): "CommsOutgoing",
    (2, 0x69CC01D9, 0x00): "EngSetCoolant",
    (2, 0x69CC01D9, 0x01): "ValueFourInts01",
    (2, 0x69CC01D9, 0x02): "LoadTube",
    (2, 0x69CC01D9, 0x03): "ConvertTorpedo",
    (2, 0x69CC01D9, 0x04): "EngSendDamcon",
    (2, 0x6AADC57F, 0x00): "AudioCommand",
    (1, 0x6D04B3DA, 0x00): "Welcome",
    (1, 0x80803DF9, 0x00): "ObjectUpdate",
    (2, 0x809305A7, 0x00): "GameMasterMessage",
    (1, 0x902F0B1A, 0x00): "Title",
    (1, 0x9AD1F23B, 0x00): "FighterBayStatus",
    (1, 0xAE88E058, 0x00): "IncomingAudio",
    (1, 0xB83FD2C4, 0x00): "BeamFired",
    (1, 0xBE991309, 0x00): "IdleText",
    (2, 0xC2BEE72E, 0x00): "FireBeam",
    (1, 0xCA88F050, 0x00): "CommsButton",
    (1, 0xCC5A3E30, 0x00): "DestroyObject",
    (1, 0xD672C35F, 0x00): "CommsIncoming",
    (1, 0xE548E74A, 0x00): "Version",
    (1, 0xEE665279, 0x00): "Intel",
    (1, 0xF5821226, 0x00): "ServerHeartbeat",
    (1, 0xF754C8FE, 0x00): "Explosion",
    (1, 0xF754C8FE, 0x01): "Klaxon",
    (1, 0xF754C8FE, 0x02): "SimpleEvent02",
    (1, 0xF754C8FE, 0x03): "SoundEffect",
    (1, 0xF754C8FE, 0x04): "Pause",
    (1, 0xF754C8FE, 0x05): "PlayerShipDamage",
    (1, 0xF754C8FE, 0x06): "EndGame",
    (1, 0xF754C8FE, 0x07): "CloakDecloak",
    (1, 0xF754C8FE, 0x08): "SimpleEvent08",
    (1, 0xF754C8FE, 0x09): "Skybox",
    (1, 0xF754C8FE, 0x0A): "GameMessage",
    (1, 0xF754C8FE, 0x0B): "EngAutoDamconUpdate",
    (1, 0xF754C8FE, 0x0C): "JumpStatusBegin",
    (1, 0xF754C8FE, 0x0D): "JumpStatusEnd",
    (1, 0xF754C8FE, 0x0E): "SimpleEvent0E",
    (1, 0xF754C8FE, 0x0F): "AllShipSettings",
    (1, 0xF754C8FE, 0x10): "DmxMessage",
    (1, 0xF754C8FE, 0x11): "KeyCaptureToggle",
    (1, 0xF754C8FE, 0x12): "Perspective",
    (1, 0xF754C8FE, 0x13): "Detonation",
    (1, 0xF754C8FE, 0x14): "GameOverReason",
    (1, 0xF754C8FE, 0x15): "GameOverStats",
    (1, 0xF754C8FE, 0x16): "SimpleEvent16",
    (1, 0xF754C8FE, 0x17): "FighterLaunched",
    (1, 0xF754C8FE, 0x18): "FighterDamage",
    (1, 0xF754C8FE, 0x19): "SimpleEvent19",
    (1, 0xF754C8FE, 0x1A): "Docked",
    (1, 0xF754C8FE, 0x1B): "Smoke",
    (1, 0xF754C8FE, 0x1C): "FighterText",
    (1, 0xF754C8FE, 0x1D): "Tag",
    (1, 0xF754C8FE, 0x1E): "GameOver",
}


subtype_lengths = {
    0x0351A5AC: 4,
    0x4C821D3C: 4,
    0x69CC01D9: 4,
    0x26FAACB9: 1,
    0xF754C8FE: 4,
}
