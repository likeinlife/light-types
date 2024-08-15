from dataclasses import dataclass
from typing import Self

from _bool_query._interface import IQ

from ._types import StringValidatorType


@dataclass(eq=False)
class LengthQ(IQ):
    _validators: list[StringValidatorType]

    def startswith(self, prefix: str) -> Self:
        self._validators.append(lambda s: s.startswith(prefix))
        return self

    def endswith(self, suffix: str) -> Self:
        self._validators.append(lambda s: s.endswith(suffix))
        return self

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
        self._validators.append(lambda s: len(s) == length)
        return self

    def custom(self, validator: StringValidatorType) -> Self:
        self._validators.append(validator)
        return self

    def compute(self, value: str) -> bool:
        return all(validator(value) for validator in self._validators)
