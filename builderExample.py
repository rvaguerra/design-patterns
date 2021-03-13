from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class RoomBuilder(ABC):

    @abstractmethod
    def buildWalls(self) -> None:
        """Build walls."""
        pass

    @abstractmethod
    def buildFloor(self) -> None:
        """Build floor."""
        pass

    @abstractmethod
    def buildCeiling(self) -> None:
        """Build ceiling."""
        pass


class ConcreteRoomBuilder(RoomBuilder):

    def buildWalls(self) -> None:
        """Build walls."""
        print('Building concrete walls.')

    def buildFloor(self) -> None:
        """Build floor."""
        print('Building concrete floor.')

    def buildCeiling(self) -> None:
        """Build ceiling."""
        print('Building concrete ceiling.')


class WoodRoomBuilder(RoomBuilder):

    def buildWalls(self) -> None:
        """Build walls."""
        print('Building wood walls.')

    def buildFloor(self) -> None:
        """Build floor."""
        print('Building wood floor.')

    def buildCeiling(self) -> None:
        """Build ceiling."""
        print('Building wood ceiling.')


class AbstractDirector(ABC):

    def __init__(self, roomBuilder: RoomBuilder) -> None:
        """Create a director instance.

        Args:
            roomBuilder (RoomBuilder): The room builder.
        """
        self.roomBuilder = roomBuilder

    @property
    def roomBuilder(self) -> RoomBuilder:
        """Get roomBuilder.

        Returns:
            RoomBuilder: The roomBuilder.
        """
        return self._roomBuilder

    @roomBuilder.setter
    def roomBuilder(self, roomBuilder: RoomBuilder) -> None:
        """Set roomBuilder.

        Args:
            roomBuilder (RoomBuilder): The roomBuilder.
        """
        self._roomBuilder = roomBuilder

    @abstractmethod
    def build(self) -> None:
        pass


class CommonDirector(AbstractDirector):

    def build(self):
        """Build!"""
        self.roomBuilder.buildFloor()
        self.roomBuilder.buildWalls()
        self.roomBuilder.buildCeiling()


class CreativeDirector(AbstractDirector):

    def build(self):
        """Build!"""
        self.roomBuilder.buildCeiling()
        self.roomBuilder.buildWalls()
        self.roomBuilder.buildFloor()


commonDirector = CommonDirector(ConcreteRoomBuilder())
commonDirector.build()

creativeDirector = CreativeDirector(ConcreteRoomBuilder())
creativeDirector.build()

doItYourself = WoodRoomBuilder()
doItYourself.buildFloor()
doItYourself.buildWalls()
doItYourself.buildCeiling()
