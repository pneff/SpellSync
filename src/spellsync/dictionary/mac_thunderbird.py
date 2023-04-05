from pathlib import Path

from spellsync.dictionary.base import Dictionary


class MacThunderbirdDictionary(Dictionary):
    """Thunderbird email client on Mac."""

    PATH_PATTERN = "Library/Thunderbird/Profiles/*/persdict.dat"
    TYPE_NAME = "mac_thunderbird"

    @classmethod
    def full_path(cls) -> Path:
        paths = list(Path("~").expanduser().glob(cls.PATH_PATTERN))
        if paths:
            return paths[0]
        else:
            raise FileNotFoundError("No Thunderbird spelling file found.")
