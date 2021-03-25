from __future__ import annotations
from observer.AbstractEventListener import AbstractEventListener
from observer.AbstractEvent import AbstractEvent
from observer.EventManager import EventManager


class ProductReleasedEvent(AbstractEvent):

    def __init__(self, productName: str) -> None:
        """Product released event. This is a concrete event, an event implementation.

        Args:
            productName (str): The name of the released product.
        """
        self.productName: str = productName

    @property
    def producName(self) -> str:
        """Get producName.

        Returns:
            str: The producName.
        """
        return self._producName

    @producName.setter
    def producName(self, producName: str) -> None:
        """Set producName.

        Args:
            producName (str): The producName.
        """
        self._producName = producName


class CustomerListener(AbstractEventListener):

    def handle(self, event: ProductReleasedEvent) -> None:
        """Invoked when the event is fired.

        Args:
            event (ProductReleasedEvent): The fired event.
        """
        print(f'Yay! The product just arrived: {event.productName}!')


listener = CustomerListener()

eventManager = EventManager()

eventManager.subscribe(ProductReleasedEvent, listener)

eventManager.notify(ProductReleasedEvent('New Laptop'))
