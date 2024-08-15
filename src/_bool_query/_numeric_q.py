from collections.abc import Callable
from dataclasses import dataclass
from decimal import Decimal
from fractions import Fraction
from typing import Self, TypeAlias

from ._base import BaseQ

NumericType: TypeAlias = int | float | Decimal | Fraction
NumericValidatorType: TypeAlias = Callable[[NumericType], bool]


@dataclass(eq=False)
class NumericQ(BaseQ[NumericType]):
    def __le__(self, number: NumericType) -> Self:
        self._validators.append(lambda n: n <= number)
        return self

    def __ge__(self, number: NumericType) -> Self:
        self._validators.append(lambda n: n >= number)
        return self

    def __gt__(self, number: NumericType) -> Self:
        self._validators.append(lambda n: n > number)
        return self

    def __lt__(self, number: NumericType) -> Self:
        self._validators.append(lambda n: n < number)
        return self
