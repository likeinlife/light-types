from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class IQ(ABC, Generic[T]):
    @abstractmethod
    def compute(self, value: T) -> bool: ...
