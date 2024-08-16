from light_types import StringQ


def test_and() -> None:
    q = (StringQ().length() > 5) & (StringQ().length() < 10)
    assert q.compute("a" * 6)
    assert not q.compute("f" * 11)


def test_or() -> None:
    q = (StringQ().length() > 5) | (StringQ().startswith("foo"))
    assert q.compute("a" * 6)
    assert q.compute("foo_")
    assert not q.compute("a")


def test_not() -> None:
    assert (~(StringQ().length() > 5)).compute("a")


def test_mixed() -> None:
    q = (StringQ().length() > 5) | (~StringQ().startswith("foo"))
    assert q.compute("a" * 6)
    assert not q.compute("foo_")
    assert q.compute("a")
