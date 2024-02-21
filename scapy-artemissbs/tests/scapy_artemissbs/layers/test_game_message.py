import pytest

from scapy_artemissbs.layers import GameMessage


class TestInit:
    @pytest.mark.parametrize(
        "bytes_, packet",
        [
            (
                b"\x11\x00\x00\x00F\x00r\x00o\x00n\x00t\x00 \x00s\x00h\x00i\x00e\x00l\x00d\x00 \x00L\x00O\x00W\x00\x00\x00",
                GameMessage(message="Front shield LOW"),
            ),
        ],
    )
    def test_bytes(self, bytes_, packet):
        assert GameMessage(bytes_) == packet
