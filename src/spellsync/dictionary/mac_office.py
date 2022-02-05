from pathlib import Path

from spellsync.dictionary.base import Dictionary


class MacOfficeDictionary(Dictionary):
    """Base class for all dictionaries."""

    PATH = Path("~/Library/Group Containers/UBF8T346G9.Office/Custom Dictionary")

    @staticmethod
    def full_path() -> Path:
        return MacOfficeDictionary.PATH.expanduser()

    @staticmethod
    def is_present() -> bool:
        """Return True if a dictionary was found on the system."""
        return MacOfficeDictionary.full_path().exists()
