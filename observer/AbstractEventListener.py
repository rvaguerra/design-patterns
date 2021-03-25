from abc import ABC, abstractmethod
from .AbstractEvent import AbstractEvent


class AbstractEventListener(ABC):

    @abstractmethod
    def handle(self, event: AbstractEvent) -> None:
        """Invoked when the event is fired.

        Args:
            event (AbstractEvent): The fired event.
        """
        pass
