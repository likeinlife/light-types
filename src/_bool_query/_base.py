from collections.abc import Callable
from dataclasses import dataclass, field
from typing import Self, TypeAlias, TypeVar

from ._interface import IQ
from ._logical import LogicMixin

T = TypeVar("T")
ValidatorType: TypeAlias = Callable[[T], bool]


@dataclass(eq=False)
class BaseQ(LogicMixin[T], IQ[T]):
    _validators: list[ValidatorType[T]] = field(default_factory=list)

    def __eq__(self, value: T) -> Self:  # type: ignore
        self._validators.append(lambda n: n == value)
        return self

    def __ne__(self, value: T) -> Self:  # type: ignore
        self._validators.append(lambda n: n != value)
        return self

    def custom(self, validator: ValidatorType[T]) -> Self:
        self._validators.append(validator)
        return self

    def compute(self, value: T) -> bool:
        return all(validator(value) for validator in self._validators)
