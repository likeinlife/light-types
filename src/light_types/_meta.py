import abc
import typing as tp

T = tp.TypeVar("T")


class LightTypeMeta(abc.ABCMeta, tp.Generic[T]):
    @classmethod
    @abc.abstractmethod
    def _parse(cls, value: T) -> T: ...

    def __call__(cls, instance: T) -> T:
        return cls._parse(instance)
