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
    class StartsWithString(LightType[str]):
        @classmethod
        def validate(cls, value: str) -> bool:
            return value.startswith("String")
    ```

    """

    @classmethod
    @abc.abstractmethod
    def validate(cls, value: T) -> bool:
        ...

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
        for i in cls.__orig_bases__:  # type: ignore
            if i.__origin__ is LightType:
                type_ = tp.get_args(i)[0]
                return isinstance(value, type_)
        return True

    @classmethod
    def __raise_error(cls, value: T) -> tp.NoReturn:
        msg = f"Could not parse {fully_qualified_name(cls)} from `{value!r}`"
        raise TypeError(msg)
