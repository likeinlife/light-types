import pytest
from light_types import LightType


def test_basic():
    class StartsWithString(LightType[str]):
        @classmethod
        def validate(cls, value: str) -> bool:
            return value.startswith("String")

    result = StartsWithString.parse("String")
    assert result
    assert isinstance(result, str)

    with pytest.raises(TypeError):
        StartsWithString.parse(1)  # type: ignore

    with pytest.raises(TypeError):
        StartsWithString.parse("NotRight")
