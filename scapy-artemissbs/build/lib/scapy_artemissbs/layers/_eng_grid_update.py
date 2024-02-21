import struct

from scapy.fields import Field
from scapy.packet import Packet

from ..fields import ArtemisSBSByteBooleanField


class SystemGridStatusField(Field):
    def getfield(self, pkt, s):
        grid_statuses = []
        while not s.startswith(b"\xff"):
            s, (x, y, z, damage) = s[7:], struct.unpack("<BBBf", s[:7])
            grid_statuses.append({"x": x, "y": y, "z": z, "damage": damage})
        s = s[1:]

        return s, grid_statuses

    def addfield(self, pkt, s, val):
        for status in val:
            s += struct.pack(
                "<BBBf", status["x"], status["y"], status["z"], status["damage"]
            )
        return s + b"\xff"


class DAMCONTeamStatusField(Field):
    def getfield(self, pkt, s):
        team_statuses = []

        while not s.startswith(b"\xfe"):
            s, values = s[33:], struct.unpack("<BIIIIIIfI", s[:33])
            team_statuses.append(
                dict(
                    zip(
                        [
                            "team_id",
                            "goal_x",
                            "current_x",
                            "goal_y",
                            "current_y",
                            "goal_z",
                            "current_z",
                            "progress",
                            "number_of_team_members",
                        ],
                        values,
                    )
                )
            )

        s = s[1:]

        return s, team_statuses

    def addfield(self, pkt, s, val):
        for status in val:
            s += struct.pack(
                "<BIIIIIIfI",
                *[
                    status[key]
                    for key in [
                        "team_id",
                        "goal_x",
                        "current_x",
                        "goal_y",
                        "current_y",
                        "goal_z",
                        "current_z",
                        "progress",
                        "number_of_team_members",
                    ]
                ]
            )
        return s + b"\xfe"


class EngGridUpdate(Packet):
    name = "Engineering Grid Update "
    fields_desc = [
        ArtemisSBSByteBooleanField("full_status", False),
        SystemGridStatusField("system_grid_status", []),
        DAMCONTeamStatusField("damcon_team_status", []),
    ]
