from light_types import LengthQ, StringQ


def test_length_q() -> None:
    q = LengthQ[list]() > 5

    assert q.compute([1, 2, 3, 4, 5, 6])
    assert not q.compute([1, 2, 3])


def test_length_q_with_string() -> None:
    q = StringQ().startswith("foo") & (LengthQ[str]() > 5)

    assert q.compute("foobar")
    assert not q.compute("a" * 6)
    assert not q.compute("foo")
