"""Tests."""
import pytest
from operations.simple import Simple


@pytest.mark.parametrize("test_input, expected", [((1, "5"), 6),
                                                  (("1", "5"), 6),
                                                  (("1", 5), 6)])
def test_simple_sum_returns_int(test_input, expected) -> None:
    """Check if accept strings."""
    sm = Simple()
    assert sm.sum(test_input[0], test_input[1]) == expected


def test_simple() -> None:
    """Test simple."""
    sm = Simple()
    assert sm.sum("1", "5") == 6
    assert sm.sum("1", 5) == 6
