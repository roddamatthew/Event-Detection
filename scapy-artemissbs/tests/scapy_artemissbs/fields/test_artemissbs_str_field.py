import pytest

from scapy_artemissbs.fields import ArtemisSBSStrField


class TestGetField:
    @pytest.mark.parametrize(
        "bytes_, val",
        [
            (b"\x04\x00\x00\x00D\x00S\x001\x00\x00\x00", "DS1"),
        ],
    )
    def test_examples(self, bytes_, val):
        assert ArtemisSBSStrField("example", "").getfield(None, bytes_) == (b"", val)


class TestGetFieldAddField:
    @pytest.mark.parametrize(
        "bytes_",
        [
            b"\x04\x00\x00\x00D\x00S\x001\x00\x00\x00",
        ],
    )
    def test_examples(self, bytes_):
        field = ArtemisSBSStrField("example", "")
        assert field.addfield(None, b"", field.getfield(None, bytes_)[1]) == bytes_
