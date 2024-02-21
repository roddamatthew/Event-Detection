import pytest

from scapy_artemissbs.layers import EngGridUpdate


class TestInit:
    @pytest.mark.parametrize(
        "bytes_, attributes",
        [
            (
                b"\x01\xff\n\x02\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x0c\x03\x00\x00\x00\x03\x00\x00\x00\x02\x00\x00\x00\x02\x00\x00\x00\x07\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\xfe",
                {
                    "full_status": True,
                    "system_grid_status": [],
                    "damcon_team_status": [
                        {
                            "current_x": 2,
                            "current_y": 0,
                            "current_z": 6,
                            "goal_x": 2,
                            "goal_y": 0,
                            "goal_z": 6,
                            "number_of_team_members": 6,
                            "progress": 0.0,
                            "team_id": 10,
                        },
                        {
                            "current_x": 0,
                            "current_y": 2,
                            "current_z": 3,
                            "goal_x": 0,
                            "goal_y": 2,
                            "goal_z": 3,
                            "number_of_team_members": 6,
                            "progress": 0.0,
                            "team_id": 11,
                        },
                        {
                            "current_x": 3,
                            "current_y": 2,
                            "current_z": 7,
                            "goal_x": 3,
                            "goal_y": 2,
                            "goal_z": 7,
                            "number_of_team_members": 6,
                            "progress": 0.0,
                            "team_id": 12,
                        },
                    ],
                },
            ),
        ],
    )
    def test_bytes(self, bytes_, attributes):
        packet = EngGridUpdate(bytes_)
        assert {attr: getattr(packet, attr) for attr in attributes} == attributes
        packet.clear_cache()
        packet.len = None
        packet.remaining = None
        assert bytes(packet) == bytes_
