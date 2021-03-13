from __future__ import annotations
from abc import ABC
from typing import Any, Generic, List, TypeVar


T = TypeVar('T')


class Composite(Generic[T or Any], ABC):

    def __init__(self, data: T or None = None, parent: Composite or None = None):
        self.data = data
        self.parent = parent
        self.children: List[Composite] = []

    @property
    def data(self) -> T or None:
        """Get data.

        Returns:
            T or None: The data.
        """
        return self._data

    @data.setter
    def data(self, data: T) -> None:
        """Set data.

        Args:
            data (T): The data.
        """
        self._data = data

    @property
    def parent(self) -> Composite or None:
        """Get parent.

        Returns:
            Component or None: The parent.
        """
        return self._parent

    @parent.setter
    def parent(self, parent: Composite or None) -> None:
        """Set parent.

        Args:
            parent (Component or None): The parent.
        """
        self._parent = parent

    @property
    def children(self) -> List[Composite]:
        """Get children.

        Returns:
            List[Composite]: The children.
        """
        return self._children

    @children.setter
    def children(self, children: List[Composite]) -> None:
        """Set children.

        Args:
            children (List[Composite]): The children.
        """
        self._children = children

    def add(self, child: Composite) -> None:
        """Add child.

        Args:
            child (Composite): The child.
        """
        self.children.append(child)
        child.parent = self

    def remove(self, child: Composite) -> None:
        """Remove child.

        Args:
            child (Composite): The child.
        """
        self.children.remove(child)
        child.parent = None
