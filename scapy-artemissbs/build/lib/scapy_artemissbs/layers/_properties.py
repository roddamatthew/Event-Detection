from typing import Sequence, List

from scapy.fields import Field

from ..fields import PropertyField
from ..fields import PropertyFlagsField


# class _FlagsChecker:
#     def __init__(self, field):
#         self.field = field
#         self._cached_flags = None
#         self._cached_flag_set = set()

#     def update(self, pkt: Packet):
#         flags = getattr(pkt, self.field.name)
#         if self._cached_flags != flags:
#             self._cached_flags = flags
#             self._cached_flag_set = set(flags)

#     def __contains__(self, field_name: str):
#         return field_name in self._cached_flag_set

#     def __call__(self, field_name: str, pkt: Packet):
#         self.update(pkt)
#         return field_name in self


def gen_fields(fields: Sequence[Field]):
    flags_field = PropertyFlagsField("flags", None, [field.name for field in fields])
    # flags_checker = _FlagsChecker(flags_field)
    wrapped_fields: List[Field] = [PropertyField(field) for field in fields]
    fields_desc: Sequence[Field] = [flags_field] + wrapped_fields
    return fields_desc
