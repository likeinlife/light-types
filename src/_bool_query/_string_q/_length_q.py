from dataclasses import dataclass
from typing import Self

from _bool_query._base import BaseQ


@dataclass(eq=False)
class LengthQ(BaseQ[str]):
    def __le__(self, length: int) -> Self:
        self._validators.append(lambda s: len(s) <= length)
        return self

    def __ge__(self, length: int) -> Self:
        self._validators.append(lambda s: len(s) >= length)
        return self

    def __gt__(self, length: int) -> Self:
        self._validators.append(lambda s: len(s) > length)
        return self

    def __lt__(self, length: int) -> Self:
        self._validators.append(lambda s: len(s) < length)
        return self

    def __eq__(self, length: int) -> Self:  # type: ignore
        self._validators.append(lambda s: len(s) == length)
        return self

    def __ne__(self, length: int) -> Self:  # type: ignore
        self._validators.append(lambda s: len(s) != length)
        return self
