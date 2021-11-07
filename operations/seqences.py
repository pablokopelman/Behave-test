"""Let's 'break' strong typing."""

from .base import Op
from typing import Any


class Seq(Op):
    """Sequential ops."""
    @staticmethod
    def sum(first: Any, second: Any) -> list:
        """Sum element by element because I say so."""
        full = list(zip(first, [int(x) for x in second]))
        return list(map(sum, full))

    @staticmethod
    def divide(first: Any, *args) -> int:
        """But division returns one value only."""
        return 1
