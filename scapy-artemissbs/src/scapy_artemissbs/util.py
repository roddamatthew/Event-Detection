from scapy.fields import FlagsField, PacketListField
from scapy.packet import NoPayload


def pretty_print_packet(packet):
    if isinstance(packet.payload, NoPayload):
        return _pretty_print_layer(packet)
    else:
        return _pretty_print_layer(packet) + "/" + pretty_print_packet(packet.payload)


def _pretty_print_layer(layer):
    return (
        type(layer).__name__
        + "("
        + ", ".join(
            _pretty_print_packet_field(layer, field) for field in layer.fields_desc
        )
        + ")"
    )


def _pretty_print_packet_field(packet, field):
    name = field.name
    value = getattr(packet, field.name)
    if isinstance(field, PacketListField):
        value_str = "[" + ",".join(pretty_print_packet(v) for v in value) + "]"
    elif isinstance(field, FlagsField):
        value_str = repr(list(value))
    else:
        value_str = repr(value)
    return f"{name}={value_str}"
