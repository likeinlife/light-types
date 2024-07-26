import abc
import typing as tp

from pydantic import GetCoreSchemaHandler
from pydantic_core import CoreSchema, core_schema

from ._meta import LightTypeMeta
from ._utils import fully_qualified_name

T = tp.TypeVar("T")


class LightType(tp.Generic[T], metaclass=LightTypeMeta):
    """Base LightType class.

    Example:
    ```python
    class StartsWithString(str, LightType):
        @classmethod
        def validate(cls, value: str) -> bool:
            return value.startswith("String")
    ```

    """

    __bounds__: type

    def __init_subclass__(cls) -> None:
        cls._discover_bounds()

    @classmethod
    @abc.abstractmethod
    def validate(cls, value: T) -> bool: ...

    @tp.final
    @classmethod
    def _parse(cls, value: T) -> T:
        checks = cls._check_type, cls.validate

        for check in checks:
            if not check(value):
                cls.__raise_error(value)

        return value

    @classmethod
    def __get_pydantic_core_schema__(
        cls,
        source_type: tp.Any,
        handler: GetCoreSchemaHandler,
    ) -> CoreSchema:
        return core_schema.no_info_before_validator_function(cls._parse, handler(str))

    @classmethod
    def _check_type(cls, value: T) -> bool:
        return isinstance(value, cls.__bounds__)

    @classmethod
    def _discover_bounds(cls) -> None:
        for type_ in cls.__mro__:
            if type_ is cls:
                continue
            if issubclass(type_, LightType):
                break
            cls.__bounds__ = type_
            return
        msg = "Can't discover bounds of LightType."
        raise RuntimeError(msg)

    @classmethod
    def __raise_error(cls, value: T) -> tp.NoReturn:
        msg = f"Could not parse {fully_qualified_name(cls)} from `{value!r}`"
        raise TypeError(msg)
