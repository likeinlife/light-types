import pytest
from light_types import LightType


def test_basic():
    class StartsWithString(str, LightType):
        @classmethod
        def validate(cls, value: str) -> bool:
            return value.startswith("String")

    result = StartsWithString("String")
    assert result
    assert isinstance(result, str)

    with pytest.raises(TypeError):
        StartsWithString(1)  # type: ignore

    with pytest.raises(TypeError):
        StartsWithString("NotRight")
