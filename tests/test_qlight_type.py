import pytest
from light_types import NumericQ, QLightType, StringQ


def test_query_startswith():
    class StartsWithString(str, QLightType):
        validator = StringQ().startswith("String")

    result = StartsWithString("String")
    assert result
    assert isinstance(result, str)

    with pytest.raises(TypeError):
        StartsWithString(1)  # type: ignore

    with pytest.raises(TypeError):
        StartsWithString("NotRight")


def test_query_custom_numeric():
    class NumericBetween5And10(int, QLightType):
        validator = (NumericQ() > 5).custom(lambda n: n < 10)

    result = NumericBetween5And10(7)
    assert result
    assert isinstance(result, int)

    with pytest.raises(TypeError):
        NumericBetween5And10("NotRight")

    with pytest.raises(TypeError):
        NumericBetween5And10(2)


def test_query_string_with_and():
    class StringWith2O(str, QLightType):
        validator = StringQ().startswith("String") & StringQ().custom(lambda s: s.count("o") >= 2)

    result = StringWith2O("Stringoo")
    assert result
    assert isinstance(result, str)

    with pytest.raises(TypeError):
        StringWith2O(1)  # type: ignore

    with pytest.raises(TypeError):
        StringWith2O("NotRight")

    with pytest.raises(TypeError):
        StringWith2O("String")
