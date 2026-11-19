"""Small utility helpers for the demo project."""


def add(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    if not name:
        return "Hello, stranger!"
    return f"Hello, {name}!"


def fib(n: int) -> list[int]:
    """Return the first n Fibonacci numbers."""
    if n <= 0:
        return []
    seq = [0]
    while len(seq) < n:
        seq.append(seq[-1] + (seq[-2] if len(seq) > 1 else 1))
    return seq
