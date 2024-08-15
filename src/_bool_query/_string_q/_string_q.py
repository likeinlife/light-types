from dataclasses import dataclass
from typing import Self

from _bool_query._base import BaseQ

from ._length_q import LengthQ


@dataclass(eq=False)
class StringQ(BaseQ[str]):
    def startswith(self, prefix: str) -> Self:
        self._validators.append(lambda s: s.startswith(prefix))
        return self

    def endswith(self, suffix: str) -> Self:
        self._validators.append(lambda s: s.endswith(suffix))
        return self

    def length(self) -> LengthQ:
        return LengthQ(self._validators)
