import pytest

from scapy_artemissbs.layers import (
    PlayerShipProperties,
)


examples = [
    (
        b"\x80(\x01\x00\x00\x00\xdblkDr\xf3.G\xef\x16\x0fG\xc0\xcdE\xc0",
        PlayerShipProperties(
            flags=["heading", "x", "z", "energy_reserves"],
            energy_reserves=941.7008666992188,
            x=44787.4453125,
            z=36630.93359375,
            heading=-3.0906829833984375,
        ),
    ),
]


class TestInit:
    @pytest.mark.parametrize("bytes_, packet", examples)
    def test_dissect(self, bytes_, packet):
        assert PlayerShipProperties(bytes_) == packet

    @pytest.mark.parametrize("bytes_, packet", examples)
    def test_build(self, bytes_, packet):
        packet = packet.copy()
        packet.flags = None
        assert bytes(packet) == bytes_
