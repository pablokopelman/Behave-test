"""Basic opertions module."""

import abc


class Op(abc.ABC):
    """docstring for Op."""

    def __init__(self, *args, **kwargs):
        """Init this thing."""
        super(Op, self).__init__()

    @staticmethod
    @abc.abstractmethod
    def sum():
        """Return the sum of the elements."""
        pass

    @staticmethod
    @abc.abstractmethod
    def divide():
        """Return the division of the elements."""
        pass
