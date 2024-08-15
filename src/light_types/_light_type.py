import typing as tp

from ._base import BaseLightType

T = tp.TypeVar("T")


class LightType(BaseLightType[T]):
    """LightType class.

    Example:
    ```python
    class StartsWithString(str, LightType):
        @classmethod
        def validate(cls, value: str) -> bool:
            return value.startswith("String")
    ```

    """

    def __init_subclass__(cls) -> None:
        cls._discover_bounds()
