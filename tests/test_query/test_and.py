from light_types import NumericQ


def test_and() -> None:
    q = (NumericQ() > 5) & (NumericQ() < 15)

    assert q.compute(10)
    assert not q.compute(20)
