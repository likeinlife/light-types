import pytest
from light_types import LightType
from pydantic import BaseModel, TypeAdapter


def test_with_pydantic() -> None:
    class StartsWithString(str, LightType):
        @classmethod
        def validate(cls, value: str) -> bool:
            return value.startswith("String")

    class MyModel(BaseModel):
        value: StartsWithString

    assert TypeAdapter(MyModel).validate_python({"value": "StringOk"})

    with pytest.raises(TypeError):
        TypeAdapter(MyModel).validate_python({"value": "InvalidString"})

    with pytest.raises(TypeError):
        TypeAdapter(MyModel).validate_python({"value": 400})
