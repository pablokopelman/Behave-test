"""Let's 'break' strong typing."""

from .base import Op
from typing import Any


def _toint(thing: Any):
    """Transform anything to int."""
    try:
        return int(thing)
    except Exception:
        print(f"{thing} is not a number!!!")
        return 0


class Simple(Op):
    """Simple math."""

    @staticmethod
    def sum(first: Any, second: Any) -> int:
        """Sum of things."""
        return _toint(first) + _toint(second)

    @staticmethod
    def divide(first: Any, second: Any) -> float:
        """Division of things."""
        return _toint(first) / _toint(second)