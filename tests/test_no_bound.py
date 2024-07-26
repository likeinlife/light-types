import pytest
from light_types import LightType


def test_no_bound():
    with pytest.raises(RuntimeError):

        class NoBoundType(LightType):
            @classmethod
            def validate(cls, value: str) -> bool:
                return value.startswith("String")
