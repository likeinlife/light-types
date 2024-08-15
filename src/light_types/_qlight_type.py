import typing as tp

from _bool_query import IQ

from ._base import BaseLightType

T = tp.TypeVar("T")


class QLightType(BaseLightType[T]):
    """Query LightType class.

    Example:
    ```python
    class StartsWithString(str, LightType):
        validator = StringQ.startswith("String")
    ```

    """

    validator: tp.ClassVar[IQ]
    __bounds__: type

    def __init_subclass__(cls) -> None:
        cls._discover_bounds()

    @tp.final
    @classmethod
    def validate(cls, value: T) -> bool:
        return cls.validator.compute(value)
