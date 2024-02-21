import pytest

from scapy_artemissbs.layers import BlackHoleProperties


class TestBuild:
    def test_simple(self):
        assert len(bytes(BlackHoleProperties(x=50000))) == 5

    @pytest.mark.parametrize(
        "packet, bytes_",
        [
            (
                BlackHoleProperties(x=10, y=20, z=30),
                b"\x07\x00\x00 A\x00\x00\xa0A\x00\x00\xf0A",
            )
        ],
    )
    def test_examples(self, packet, bytes_):
        assert bytes(packet) == bytes_
