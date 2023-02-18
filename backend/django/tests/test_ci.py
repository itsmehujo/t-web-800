import pytest

def inc(x):
    return x + 1


def test_should_fail():
    assert inc(3) == 5