import pytest

from scapy_artemissbs.fields import ArtemisSBSFlagsField

# a  b  c  d  e  f  g  h  i  j  k  l  m  n
# 0  1  2  3  4  5  6  7  8  9  10 11 12 13
# 13 12 11 10 9  8  7  6  5  4  3  2  1  0
#


class TestGetField:
    @pytest.mark.parametrize(
        "field, bytes_, value",
        [
            (
                ArtemisSBSFlagsField("flags", 0, list("abcdefghijklmn")),
                b"\x01\x00",
                "a",
            ),
            (
                ArtemisSBSFlagsField("flags", 0, list("abcdefghijklmn")),
                b"\x02\x00",
                "b",
            ),
            (
                ArtemisSBSFlagsField("flags", 0, list("abcdefghijklmn")),
                b"\x04\x00",
                "c",
            ),
            (
                ArtemisSBSFlagsField("flags", 0, list("abcdefghijklmn")),
                b"\x00\x01",
                "i",
            ),
            (
                ArtemisSBSFlagsField("flags", 0, list("abcdefghijklmn")),
                b"\x00\x02",
                "j",
            ),
            (
                ArtemisSBSFlagsField("flags", 0, list("abcdefghijklmn")),
                b"\x00\x04",
                "k",
            ),
            (
                ArtemisSBSFlagsField("flags", 0, list("abcdefghijklmn")),
                b"\x00\x08",
                "l",
            ),
            (
                ArtemisSBSFlagsField("flags", 0, list("abcdefghijklmn")),
                b"\x00\x10",
                "m",
            ),
            (
                ArtemisSBSFlagsField("flags", 0, list("abcdefghijklmn")),
                b"\x00\x20",
                "n",
            ),
        ],
    )
    def test_examples(self, field, bytes_, value):
        assert field.getfield(None, bytes_) == (b"", value)
