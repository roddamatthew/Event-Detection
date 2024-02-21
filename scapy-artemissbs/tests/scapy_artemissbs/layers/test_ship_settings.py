import pytest

from scapy_artemissbs.layers import ShipSettings


class TestInit:
    @pytest.mark.parametrize(
        "bytes_, packet",
        [
            (
                b"\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x08\x00\x00\x00A\x00r\x00t\x00e\x00m\x00i\x00s\x00\x00\x00",
                ShipSettings(
                    drive_type="warp",
                    hull_id=4,
                    accent_color=0.0,
                    name="Artemis",
                ),
            ),
            (
                b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x01\x00\x00\x00\t\x00\x00\x00I\x00n\x00t\x00r\x00e\x00p\x00i\x00d\x00\x00\x00",
                ShipSettings(
                    drive_type="warp",
                    hull_id=0,
                    accent_color=0.125,
                    name="Intrepid",
                ),
            ),
        ],
    )
    def test_bytes(self, bytes_, packet):
        dispacket = ShipSettings(bytes_)
        assert dispacket == packet
        dispacket.clear_cache()
        assert bytes(dispacket) == bytes_
