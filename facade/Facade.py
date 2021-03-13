from __future__ import annotations
from typing import Any


class Facade:

    def _processData(self, data: Any) -> Any:
        """Process provided data.

        Args:
            data (Any): The data.

        Returns:
            Any: The output.
        """
        return 'output'

    def operationA(self, data: Any) -> Any:
        """Process given data hiding complex logic from the client.

        Args:
            data (Any): The data.

        Returns:
            Any: The output.
        """
        return self._processData(data)
