import pytest

from scapy_artemissbs.layers import Version


class TestInit:
    @pytest.mark.parametrize(
        "bytes_, attributes",
        [
            (
                b"\xa4\n\x00\x00\x00\x00\x00@\x02\x00\x00\x00\x07\x00\x00\x00\x02\x00\x00\x00",
                {"version": "2.7.2"},
            )
        ],
    )
    def test_simple(self, bytes_, attributes):
        packet = Version(bytes_)
        assert {attr: getattr(packet, attr) for attr in attributes} == attributes
        packet.clear_cache()
        packet.remove_payload()
        assert bytes(packet) == bytes_
