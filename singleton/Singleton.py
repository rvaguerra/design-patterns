from __future__ import annotations


class _SingletonMetaclass(type):
    """Singleton metaclass."""

    _instances: dict = {}

    def __call__(cls, *args, **kwargs) -> _SingletonMetaclass:
        """Invoked when class is called. Replaces class with stored instance.

        Returns:
            _SingletonMetaclass: The class instance.
        """
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]


class Singleton(metaclass=_SingletonMetaclass):
    """Singleton class."""

    pass
