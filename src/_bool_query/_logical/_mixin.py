from typing import TypeVar

from _bool_query._interface import IQ

T = TypeVar("T")


class LogicMixin(IQ[T]):
    def __or__(self, other: IQ[T]) -> IQ[T]:
        from ._or import OrQ

        return OrQ(self, other)

    def __invert__(self) -> IQ[T]:
        from ._not import NotQ

        return NotQ(self)

    def __and__(self, other: IQ[T]) -> IQ[T]:
        from ._and import AndQ

        return AndQ(self, other)
