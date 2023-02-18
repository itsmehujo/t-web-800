import pytest

def inc(x):
    return x + 1


def test_should_work():
    assert inc(3) == 4