from pathlib import Path

from spellsync.dictionary.base import Dictionary


class MacOfficeDictionary(Dictionary):
    """Base class for all dictionaries."""

    PATH = Path("~/Library/Group Containers/UBF8T346G9.Office/Custom Dictionary")

    def __init__(self) -> None:
        super().__init__()
        with self.full_path().open("r", encoding="utf-16") as f:
            for line in f:
                self.words.add(line.strip())

    @staticmethod
    def full_path() -> Path:
        return MacOfficeDictionary.PATH.expanduser()

    @staticmethod
    def is_present() -> bool:
        """Return True if a dictionary was found on the system."""
        return MacOfficeDictionary.full_path().exists()
