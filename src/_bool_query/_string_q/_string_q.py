from dataclasses import dataclass, field
from typing import Self

from _bool_query._interface import IQ

from ._length_q import LengthQ
from ._types import StringValidatorType


@dataclass(eq=False)
class StringQ(IQ[str]):
    _validators: list[StringValidatorType] = field(default_factory=list)

    def startswith(self, prefix: str) -> Self:
        self._validators.append(lambda s: s.startswith(prefix))
        return self

    def endswith(self, suffix: str) -> Self:
        self._validators.append(lambda s: s.endswith(suffix))
        return self

    def length(self) -> LengthQ:
        return LengthQ(self._validators)

    def __eq__(self, string: str) -> Self:  # type: ignore
        self._validators.append(lambda s: s == string)
        return self

    def __ne__(self, string: str) -> Self:  # type: ignore
        self._validators.append(lambda s: s == string)
        return self

    def custom(self, validator: StringValidatorType) -> Self:
        self._validators.append(validator)
        return self

    def compute(self, value: str) -> bool:
        return all(validator(value) for validator in self._validators)
