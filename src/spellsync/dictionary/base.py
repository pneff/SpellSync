from abc import abstractmethod
from typing import Generator


class Dictionary:
    """Base class for all dictionaries."""

    words: set[str]

    def __init__(self) -> None:
        self.words = set()

    @staticmethod
    @abstractmethod
    def is_present() -> bool:
        """Return True if a dictionary was found on the system."""
        pass

    def __iter__(self) -> Generator[str, None, None]:
        yield from self.words

    def __len__(self) -> int:
        return len(self.words)
