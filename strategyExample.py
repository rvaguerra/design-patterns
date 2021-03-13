from __future__ import annotations
from strategy import Context, Strategy, StrategyData


class MathContext(Context[float]):
    """The math context. Requires no implementation, but defines output type.

    Args:
        Context (Context[float]): The context abstract class.
    """
    pass


class OperationData(StrategyData):
    """Stores operation data.

    Args:
        StrategyData (StrategyData): The strategy data abstract class.
    """

    def __init__(self, a: float, b: float) -> None:
        """Create an operation data instance.

        Args:
            a (float): First number.
            b (float): Second number.
        """
        self.a = a
        self.b = b

    @property
    def a(self) -> float:
        """Get a.

        Returns:
            float: The a.
        """
        return self._a

    @a.setter
    def a(self, a: float) -> None:
        """Set a.

        Args:
            a (float): The a.
        """
        self._a = a

    @property
    def b(self) -> float:
        """Get b.

        Returns:
            float: The b.
        """
        return self._b

    @b.setter
    def b(self, b: float) -> None:
        """Set b.

        Args:
            b (float): The b.
        """
        self._b = b


class MultiplyStrategy(Strategy[float]):
    """Multiply strategy.

    Args:
        Strategy (Strategy[float]): The strategy abstract class.
    """

    def execute(self, data: OperationData) -> float:
        """Execute strategy.

        Args:
            data (OperationData): The data to be handled.

        Returns:
            float: The execution output.
        """
        return data.a * data.b


class AddStrategy(Strategy[float]):
    """Add strategy.

    Args:
        Strategy (Strategy[float]): The strategy abstract class.
    """

    def execute(self, data: OperationData) -> float:
        """Execute strategy.

        Args:
            data (OperationData): The data to be handled.

        Returns:
            float: The execution output.
        """
        return data.a + data.b


data = OperationData(2, 5)

strategies = [
    AddStrategy(),
    MultiplyStrategy(),
]

for strategy in strategies:
    print(MathContext(strategy, data).execute().data)
