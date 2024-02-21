import pytest

from scapy_artemissbs.layers import (
    EngineeringConsoleProperties,
)


class TestInit:
    @pytest.mark.parametrize(
        "bytes_, packet",
        [
            (
                b"\xf7\x00\x00\x00\xa7\x7fB:\xa7\x7fB:\xa7\x7fB:\xa7\x7fB:\xa7\x7fB:\xa7\x7fB:\xa7\x7fB:",
                EngineeringConsoleProperties(
                    flags="heat_level_1+heat_level_2+heat_level_3+heat_level_5+heat_level_6+heat_level_7+heat_level_8",
                    heat_level_1=0.0007419534376822412,
                    heat_level_2=0.0007419534376822412,
                    heat_level_3=0.0007419534376822412,
                    heat_level_5=0.0007419534376822412,
                    heat_level_6=0.0007419534376822412,
                    heat_level_7=0.0007419534376822412,
                    heat_level_8=0.0007419534376822412,
                ),
            ),
        ],
    )
    def test_dissect(self, bytes_, packet):
        assert EngineeringConsoleProperties(bytes_) == packet
