from dataclasses import dataclass
from typing import TypeVar

from _bool_query._interface import IQ

from ._mixin import LogicMixin

T = TypeVar("T")


@dataclass(frozen=True, eq=False, slots=True)
class AndQ(LogicMixin[T], IQ[T]):
    first: IQ[T]
    second: IQ[T]

    def compute(self, value: T) -> bool:
        return self.first.compute(value) and self.second.compute(value)
