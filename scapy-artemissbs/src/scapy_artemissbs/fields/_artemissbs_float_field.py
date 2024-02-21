from scapy.fields import Field


class ArtemisSBSFloatField(Field[int, int]):
    def __init__(self, name, default):
        Field.__init__(self, name, default, "<f")  # There was some problem using super() here, haven't been able to work out why.
