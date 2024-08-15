from collections.abc import Callable
from typing import TypeAlias

StringValidatorType: TypeAlias = Callable[[str], bool]
