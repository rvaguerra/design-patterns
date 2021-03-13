from __future__ import annotations
from abc import ABC
from typing import Generic, TypeVar


T = TypeVar('T')


class StrategyResult(Generic[T], ABC):
    """Strategy result class to store executed output.

    Args:
        Generic (T): The type of output.
        ABC (ABCMeta): The meta class.
    """

    def __init__(self, data: T) -> None:
        """Create a strategy result instance.

        Args:
            data (T): The result data.
        """
        self.data = data

    @property
    def data(self) -> T:
        """Get data.

        Returns:
            T: The data.
        """
        return self._data

    @data.setter
    def data(self, data: T) -> None:
        """Set data.

        Args:
            data (T): The data.
        """
        self._data = data
