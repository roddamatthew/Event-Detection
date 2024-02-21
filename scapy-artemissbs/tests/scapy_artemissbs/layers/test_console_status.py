import pytest

from scapy_artemissbs.layers import ConsoleStatus


class TestInit:
    @pytest.mark.parametrize(
        "bytes_, attributes",
        [
            (
                b"\x00\x00\x00\x00\x00\x01\x02\x02\x01\x00\x00\x00\x00\x00\x00",
                {
                    "ship_number": 0,
                    "main_screen": 0,
                    "helm": 1,
                    "weapons": 2,
                    "engineering": 2,
                    "science": 1,
                    "communications": 0,
                    "single_seat_craft": 0,
                    "data": 0,
                    "observer": 0,
                    "captains_map": 0,
                    "game_master": 0,
                },
            ),
        ],
    )
    def test_bytes(self, bytes_, attributes):
        packet = ConsoleStatus(bytes_)
        assert {attr: getattr(packet, attr) for attr in attributes} == attributes
        packet.clear_cache()
        packet.len = None
        packet.remaining = None
        assert bytes(packet) == bytes_
