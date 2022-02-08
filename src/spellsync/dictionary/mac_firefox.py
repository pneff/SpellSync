from pathlib import Path

from spellsync.dictionary.base import Dictionary


class MacFirefoxDictionary(Dictionary):
    """Base class for all dictionaries."""

    PATH_PATTERN = "Library/ApplicationSupport/Firefox/Profiles/*/persdict.dat"
    TYPE_NAME = "mac_firefox"

    @classmethod
    def full_path(cls) -> Path:
        paths = list(Path("~").expanduser().glob(cls.PATH_PATTERN))
        if paths:
            return paths[0]
        else:
            raise FileNotFoundError("No Firefox spelling file found.")
