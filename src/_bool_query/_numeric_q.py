from collections.abc import Callable
from dataclasses import dataclass, field
from decimal import Decimal
from fractions import Fraction
from typing import Self, TypeAlias

from ._interface import IQ

NumericType: TypeAlias = int | float | Decimal | Fraction
NumericValidatorType: TypeAlias = Callable[[NumericType], bool]


@dataclass(eq=False)
class NumericQ(IQ[NumericType]):
    _validators: list[NumericValidatorType] = field(default_factory=list)

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

    def __eq__(self, number: NumericType) -> Self:  # type: ignore
        self._validators.append(lambda n: n == number)
        return self

    def __ne__(self, number: NumericType) -> Self:  # type: ignore
        self._validators.append(lambda n: n != number)
        return self

    def custom(self, validator: NumericValidatorType) -> Self:
        self._validators.append(validator)
        return self

    def compute(self, value: NumericType) -> bool:
        return all(validator(value) for validator in self._validators)
