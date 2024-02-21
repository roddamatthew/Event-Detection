import pytest

from scapy_artemissbs.layers import (
    ArtemisSBS,
    CommsOutgoing,
    DroneProperties,
    EngSendDamcon,
    GameMessage,
    ObjectUpdate,
    ToggleShields,
    SimpleEvent19,
    SingleObjectUpdate,
    Smoke,
    Tag,
)


class TestInit:
    @pytest.mark.parametrize(
        "bytes_, packet",
        [
            (
                b"\xef\xbe\xad\xde \x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00<\x1d\x82L\x04\x00\x00\x00\x00\x00\x00\x00",
                ArtemisSBS(
                    header=0xDEADBEEF,
                    len=32,
                    padding=0,
                    remaining=12,
                    origin=2,
                    internal_type=0x4C821D3C,
                    internal_subtype=0x04,
                    type="ToggleShields",
                )
                / ToggleShields(padding=0),
            ),
            (
                b"\xef\xbe\xad\xde \x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00\xfe\xc8T\xf7\x19\x00\x00\x00\x00\x00\x00\x00",
                ArtemisSBS(
                    header=0xDEADBEEF,
                    len=32,
                    padding=0,
                    remaining=12,
                    type="SimpleEvent19",
                )
                / SimpleEvent19(),
            ),
            (
                b"\xef\xbe\xad\xde\x1c\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00<\x1d\x82L$\x00\x00\x00",
                ArtemisSBS(
                    header=0xDEADBEEF,
                    len=28,
                    padding=0,
                    origin=2,
                    remaining=8,
                    internal_type="valueInt",
                    internal_subtype=0x24,
                    type="ClientHeartbeat",
                ),  # / RequestEngGridUpdate(),
            ),
            (
                bytes.fromhex(
                    "efbeadde2c000000020000000000000018000000d901cc690400000000000000010000000200000006000000"
                ),
                ArtemisSBS(
                    header=0xDEADBEEF,
                    len=44,
                    origin="client",
                    padding=0,
                    remaining=24,
                    internal_type="valueFourInts",
                    internal_subtype=0x4,
                    type="EngSendDamcon",
                )
                / EngSendDamcon(team_number=0, x=1, y=2, z=6),
            ),
            (
                bytes.fromhex(
                    "efbeadde2c0000000200000000000000180000004b4c4c5703000000b40600000000000000000000c8f8af00"
                ),
                ArtemisSBS(
                    header=0xDEADBEEF,
                    len=44,
                    origin="client",
                    padding=0,
                    remaining=24,
                    internal_type="commsMessage",
                    internal_subtype=0x0,
                    type="CommsOutgoing",
                )
                / CommsOutgoing(
                    comm_target_type="other",
                    recipient_id=1716,
                    message=0,
                    target_object_id=0,
                    unknown=11532488,
                ),
            ),
            (
                bytes.fromhex(
                    "efbeadde5000000001000000000000003c000000fec854f71d000000cc0500000000000007000000470061006e0064006800690000000b00000032003000300032002d00310031002d00320036000000"
                ),
                ArtemisSBS(
                    header=0xDEADBEEF,
                    len=80,
                    origin="server",
                    padding=0,
                    remaining=60,
                    internal_type="simpleEvent",
                    internal_subtype=0x1D,
                    type="Tag",
                )
                / Tag(object_id=1484, unknown=0, tagger="Gandhi", date="2002-11-26"),
            ),
            (
                b"\xef\xbe\xad\xde0\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\x00\xfe\xc8T\xf7\x1b\x00\x00\x00`\t\x00\x00\x02\x00\x00\x00\xa6fCBF\x8d\xc1\xbe\x87W\x0b\xc2",
                ArtemisSBS(
                    header=0xDEADBEEF,
                    len=48,
                    origin="server",
                    padding=0,
                    remaining=28,
                    internal_type="simpleEvent",
                    internal_subtype=0x1B,
                    type="Smoke",
                )
                / Smoke(
                    object_id=2400,
                    priority=2,
                    x=48.850242614746094,
                    y=-0.3780309557914734,
                    z=-34.83547592163086,
                ),
            ),
            (
                b"\xef\xbe\xad\xdeB\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00.\x00\x00\x00\xfe\xc8T\xf7\n\x00\x00\x00\x11\x00\x00\x00F\x00r\x00o\x00n\x00t\x00 \x00s\x00h\x00i\x00e\x00l\x00d\x00 \x00L\x00O\x00W\x00\x00\x00",
                ArtemisSBS(
                    header=0xDEADBEEF,
                    len=66,
                    origin="server",
                    padding=0,
                    remaining=46,
                    internal_type="simpleEvent",
                    internal_subtype=0xA,
                    type="GameMessage",
                )
                / GameMessage(message="Front shield LOW"),
            ),
            (
                b"\xef\xbe\xad\xdeC\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00/\x00\x00\x00\xf9=\x80\x80\x10\xe9\t\x00\x00\xff\x00\x1e\x00\x00\x006\x16WG\x14\x87(>\xb0\xee3G\x00\x00\x00\x00(\\\x0f>\x0e-\x9d\xbf\x01\x00\x00\x00\x00\x00\x00\x00",
                ArtemisSBS(
                    header=0xDEADBEEF,
                    len=67,
                    origin="server",
                    padding=0,
                    remaining=47,
                    internal_type="objectBitStream",
                    internal_subtype=0x0,
                    type="ObjectUpdate",
                )
                / ObjectUpdate(
                    updates=[
                        SingleObjectUpdate(object_type=16, object_id=2537)
                        / DroneProperties(
                            flags=65280,
                            unknown_1p1=30,
                            x=55062.2109375,
                            y=0.16457778215408325,
                            z=46062.6875,
                            unknown_1p5=0.0,
                            unknown_1p6=0.13999998569488525,
                            heading=-1.2279374599456787,
                            side=1,
                        )
                    ],
                    padding=0,
                ),
            ),
        ],
    )
    def test_dissect(self, bytes_, packet):
        assert ArtemisSBS(bytes_) == packet

    @pytest.mark.parametrize(
        "packet, bytes_",
        [
            (
                ArtemisSBS() / ToggleShields(),
                b"\xef\xbe\xad\xde \x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x00\x00<\x1d\x82L\x04\x00\x00\x00\x00\x00\x00\x00",
            )
        ],
    )
    def test_build(self, bytes_, packet):
        assert bytes(packet) == bytes_

    def test_defaults(self):
        assert ArtemisSBS() == ArtemisSBS(origin=1, type="ObjectUpdate")
