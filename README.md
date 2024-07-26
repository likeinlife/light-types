# Light Types

[![image](https://img.shields.io/pypi/v/light-types.svg)](https://pypi.python.org/pypi/light-types)
[![codecov](https://codecov.io/gh/likeinlife/light-types/graph/badge.svg?token=7QUSPNC4CQ)](https://codecov.io/gh/likeinlife/light-types)
[![Rye](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/rye/main/artwork/badge.json)](https://rye.astral.sh)
[![image](https://img.shields.io/pypi/l/light-types.svg)](https://github.com/likeinlife/error_mapper/blob/main/LICENSE)
<a href="http://mypy-lang.org/" target="_blank"><img src="https://img.shields.io/badge/mypy-checked-1F5082.svg" alt="Mypy checked"></a>
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![image](https://img.shields.io/pypi/pyversions/light-types.svg)](https://pypi.python.org/pypi/light-types)

"Parse, don't validate"

Compatible with PydanticV2

Inspired by [Phantom types](https://github.com/antonagestam/phantom-types/)

# Examples

## Sample

```python
from light_types import LightType


class StartsWithString(LightType[str]):
    @classmethod
    def validate(cls, value: str) -> bool:
        return value.startswith("String")
```

## With Pydantic

```python
from light_types import LightType


class StartsWithString(LightType[str]):
    @classmethod
    def validate(cls, value: str) -> bool:
        return value.startswith("String")

class MyModel(BaseModel):
    value: StartsWithString

assert TypeAdapter(MyModel).validate_python({"value": "StringOk"})
```

# Tests, linting, formatting

- `rye test | lint | fmt`