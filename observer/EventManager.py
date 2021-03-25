from __future__ import annotations
from typing import Dict, List
from .AbstractEvent import AbstractEvent
from .AbstractEventListener import AbstractEventListener


EventMap = Dict[str, List[AbstractEventListener]]


class EventManager:

    def __init__(self) -> None:
        self._events: EventMap = {}

    @property
    def events(self) -> EventMap:
        """Get events.

        Returns:
            EventMap: The events.
        """
        return self._events

    def subscribe(self, event: AbstractEvent, listener: AbstractEventListener) -> None:
        if event not in self.events:
            self.events[event.__name__] = []

        self.events[event.__name__].append(listener)

    def notify(self, event: AbstractEvent) -> None:
        if event.__class__.__name__ not in self.events:
            return

        for listener in self.events[event.__class__.__name__]:
            listener.handle(event)
