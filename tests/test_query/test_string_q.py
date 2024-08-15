from light_types import StringQ


def test_startswith() -> None:
    q = StringQ()

    q.startswith("foo")
    assert q.compute("foo")
    assert not q.compute("fo")

    q.startswith("foobar")

    assert q.compute("foobar")
    assert not q.compute("fo")


def test_comparing() -> None:
    q = StringQ() == "foo"

    assert q.compute("foo")
    assert not q.compute("not-foo")


def test_comparing_mixed() -> None:
    q = 1 < StringQ().startswith("foo").length() < 5

    assert q.compute("foo")
    assert not q.compute("not-foo")
    assert not q.compute("")


def test_comparing_length() -> None:
    q = 1 < StringQ().length() < 10

    assert q.compute("foo")
    assert not q.compute("")
    assert not q.compute("a" * 11)


def test_comparing_length_equal() -> None:
    q = StringQ().length() == 10

    assert q.compute("a" * 10)
