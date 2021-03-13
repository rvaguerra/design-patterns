class Source:

    def message(self) -> str:
        """Retrieve source message.

        Returns:
            str: The source message.
        """
        return '.tegraT'


class Target:

    def message(self) -> str:
        """Retrieve target message.

        Returns:
            str: The target message.
        """
        return 'Target.'


class SourceToTargetAdapter(Target):

    def __init__(self, source: Source) -> None:
        """Encapsulates source.

        Args:
            source (Source): Source instance.
        """
        self.source = source

    @property
    def source(self) -> Source:
        """Get source.

        Returns:
            Source: The source.
        """
        return self._source

    @source.setter
    def source(self, source: Source) -> None:
        """Set source.

        Args:
            source (Source): The source.
        """
        self._source = source

    def message(self) -> str:
        return self.source.message()[::-1]


class RequiresTarget:

    def __init__(self, target: Target) -> None:
        """Component that requires target.

        Args:
            target (Target): The target.
        """
        self.target = target

    @property
    def target(self) -> Target:
        """Get target.

        Returns:
            Target: The target.
        """
        return self._target

    @target.setter
    def target(self, target: Target) -> None:
        """Set target.

        Args:
            target (Target): The target.
        """
        self._target = target


adaptedSource = SourceToTargetAdapter(Source())
target = Target()

print(adaptedSource.message() == target.message())

RequiresTarget(adaptedSource)
