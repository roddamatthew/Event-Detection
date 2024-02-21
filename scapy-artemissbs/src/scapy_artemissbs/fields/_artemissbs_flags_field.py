import math
from typing import Any, Optional, Union, List

from scapy.fields import FlagValue, FlagsField


def ljust_list(list_: List, length, fill_value):
    return list_ + (length - len(list_)) * [fill_value]


class ArtemisSBSFlagsField(FlagsField):
    def __init__(
        self,
        name: str,
        default: Optional[Union[int, FlagValue]],
        names: List[str],
        fill_prefix="unused",
    ) -> None:
        size = len(names)
        n_bytes = (size // 8 + 1) if (size % 8 == 0) else int(math.ceil(size / 8))
        padding = n_bytes * 8 - size

        reordered_names: List[str] = []
        for i in range(n_bytes):
            reordered_names = (
                ljust_list(names[8 * i : 8 * (i + 1)], 8, fill_prefix) + reordered_names
            )

        super().__init__(name, default, size + padding, reordered_names)
