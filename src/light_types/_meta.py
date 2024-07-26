import abc
import typing as tp

T = tp.TypeVar("T")


class LightTypeMeta(abc.ABCMeta):
    @classmethod
    @abc.abstractmethod
    def parse(cls, value: T) -> T: ...

    def __call__(cls, instance: object) -> object:
        return cls.parse(instance)
