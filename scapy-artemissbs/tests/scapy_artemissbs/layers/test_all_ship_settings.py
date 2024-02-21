import pytest

from scapy_artemissbs.layers import AllShipSettings, ShipSettings


class TestInit:
    @pytest.mark.parametrize(
        "bytes_, packet",
        [
            (
                b"\x00\x00\x00\x00\x04\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x08\x00\x00\x00A\x00r\x00t\x00e\x00m\x00i\x00s\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x01\x00\x00\x00\t\x00\x00\x00I\x00n\x00t\x00r\x00e\x00p\x00i\x00d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80>\x01\x00\x00\x00\x06\x00\x00\x00A\x00e\x00g\x00i\x00s\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0>\x01\x00\x00\x00\x08\x00\x00\x00H\x00o\x00r\x00a\x00t\x00i\x00o\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x01\x00\x00\x00\n\x00\x00\x00E\x00x\x00c\x00a\x00l\x00i\x00b\x00u\x00r\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 ?\x01\x00\x00\x00\x05\x00\x00\x00H\x00e\x00r\x00a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@?\x01\x00\x00\x00\x06\x00\x00\x00C\x00e\x00r\x00e\x00s\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`?\x01\x00\x00\x00\x06\x00\x00\x00D\x00i\x00a\x00n\x00a\x00\x00\x00",
                AllShipSettings(
                    ships=[
                        ShipSettings(
                            drive_type="warp",
                            hull_id=4,
                            accent_color=0.0,
                            name="Artemis",
                        ),
                        ShipSettings(
                            drive_type="warp",
                            hull_id=0,
                            accent_color=0.125,
                            name="Intrepid",
                        ),
                        ShipSettings(
                            drive_type="warp",
                            hull_id=0,
                            accent_color=0.25,
                            name="Aegis",
                        ),
                        ShipSettings(
                            drive_type="warp",
                            hull_id=0,
                            accent_color=0.375,
                            name="Horatio",
                        ),
                        ShipSettings(
                            drive_type="warp",
                            hull_id=0,
                            accent_color=0.5,
                            name="Excalibur",
                        ),
                        ShipSettings(
                            drive_type="warp",
                            hull_id=0,
                            accent_color=0.625,
                            name="Hera",
                        ),
                        ShipSettings(
                            drive_type="warp",
                            hull_id=0,
                            accent_color=0.75,
                            name="Ceres",
                        ),
                        ShipSettings(
                            drive_type="warp",
                            hull_id=0,
                            accent_color=0.875,
                            name="Diana",
                        ),
                    ]
                ),
            ),
        ],
    )
    def test_bytes(self, bytes_, packet):
        dispacket = AllShipSettings(bytes_)
        assert dispacket == packet
        dispacket.clear_cache()
        dispacket.len = None
        dispacket.remaining = None
        assert bytes(dispacket) == bytes_
