import pytest

from scapy_artemissbs.layers import (
    NPCShipProperties,
)


examples = [
    (
        b"\x84\x1b\x00\x00\x00\x00\x00\xdc%\xdf>\x90\xed\xf0F\xcd\x8a\xae\xc2\xd5\xde\x96G\tu\xf0=.y\xf0?",
        NPCShipProperties(
            flags="y+z+roll+heading+rudder+x",
            rudder=0.43583571910858154,
            x=30838.78125,
            y=-87.2710952758789,
            z=77245.6640625,
            roll=0.11741072684526443,
            heading=1.8786981105804443,
        ),
    )
]


class TestInit:
    @pytest.mark.parametrize(
        "bytes_, packet",
        examples,
    )
    def test_dissect(self, bytes_, packet):
        assert NPCShipProperties(bytes_) == packet

    @pytest.mark.parametrize(
        "bytes_, packet",
        examples,
    )
    def test_build(self, bytes_, packet):
        packet = packet.copy()
        packet.flags = None
        assert bytes(packet) == bytes_
