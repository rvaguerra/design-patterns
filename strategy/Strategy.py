from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from .StrategyData import StrategyData


T = TypeVar('T')


class Strategy(Generic[T], ABC):
    """A strategy.

    Args:
        Generic (T): The output type.
        ABC (ABCMeta): The meta class.
    """

    @abstractmethod
    def execute(self, data: StrategyData) -> T:
        """Execute strategy.

        Args:
            data (StrategyData): The data to be handled.

        Returns:
            T: The execution output.
        """
        pass
