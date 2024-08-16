from dataclasses import dataclass
from typing import TypeVar

from _bool_query._interface import IQ

from ._mixin import LogicMixin

T = TypeVar("T")


@dataclass(frozen=True, eq=False, slots=True)
class NotQ(LogicMixin[T], IQ[T]):
    query: IQ[T]

    def compute(self, value: T) -> bool:
        return not self.query.compute(value)
