from typing import Generic, TypeVar
from .Strategy import Strategy
from .StrategyData import StrategyData
from .StrategyResult import StrategyResult


T = TypeVar('T')


class Context(Generic[T]):
    """Context.

    Args:
        Generic (T): The output type.
    """

    def __init__(self, strategy: Strategy[T], data: StrategyData) -> None:
        """Create a context instance.

        Args:
            strategy (Strategy[T]): The selected strategy.
            data (StrategyData): The data to be handled.
        """
        self.strategy = strategy
        self.data = data

    @property
    def strategy(self) -> Strategy[T]:
        """Get strategy.

        Returns:
            Strategy[T]: The strategy.
        """
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy[T]) -> None:
        """Set strategy.

        Args:
            strategy (Strategy[T]): The strategy.
        """
        self._strategy = strategy

    @property
    def data(self) -> StrategyData:
        """Get data.

        Returns:
            StrategyData: The data.
        """
        return self._data

    @data.setter
    def data(self, data: StrategyData) -> None:
        """Set data.

        Args:
            data (StrategyData): The data.
        """
        self._data = data

    def execute(self) -> StrategyResult[T]:
        """Execute strategy.

        Returns:
            StrategyResult[T]: The output.
        """
        return StrategyResult[T](self.strategy.execute(self.data))
