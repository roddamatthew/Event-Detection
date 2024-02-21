from scapy.fields import Field, LEIntField


class ArtemisSBSBooleanField(Field):
    __slots__ = ["_field"]

    def __init__(self, name, default):
        super().__init__(name, default)
        self._field = LEIntField(name, 0)

    def getfield(self, pkt, s):
        s, flag = self._field.getfield(pkt, s)
        return s, bool(flag)

    def addfield(self, pkt, s, val):
        return self._field.addfield(pkt, s, int(val))
