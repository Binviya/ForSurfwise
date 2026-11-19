import pytest

from src.utils import add, fib, greet


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_greet():
    assert greet("Alice") == "Hello, Alice!"


def test_fib():
    assert fib(0) == []
    assert fib(1) == [0]
    assert fib(5) == [0, 1, 1, 2, 3]
