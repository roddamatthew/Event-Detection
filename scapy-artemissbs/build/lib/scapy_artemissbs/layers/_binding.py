from scapy.packet import bind_layers
from scapy.layers.inet import TCP

from ._artemissbs import ArtemisSBS


def do_binding(bindings, layers):
    for (origin, internal_type, internal_subtype), type_name in bindings.items():
        if (layer := layers.get(type_name)) is not None:
            bind_layers(
                ArtemisSBS,
                layer,
                origin=origin,
                internal_type=internal_type,
                internal_subtype=internal_subtype,
            )
