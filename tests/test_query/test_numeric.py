from light_types import NumericQ


def test_comparing() -> None:
    q = 5 < NumericQ() < 15

    assert q.compute(10)
    assert not q.compute(20)


def test_comparing_or_eq() -> None:
    q = 5 <= NumericQ() <= 15

    assert q.compute(5)
    assert not q.compute(4)


def test_comparing_equal() -> None:
    q = NumericQ() == 5
    assert q.compute(5)
    assert not q.compute(4)


def test_comparing_not_equal() -> None:
    q = NumericQ() != 5
    assert q.compute(4)
    assert not q.compute(5)


def test_custom() -> None:
    q = NumericQ().custom(lambda n: n % 2 == 0)
    assert q.compute(2)
    assert not q.compute(3)
