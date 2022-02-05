from pathlib import Path

from spellsync.dictionary.base import Dictionary


class MacOfficeDictionary(Dictionary):
    """Base class for all dictionaries."""

    PATH = Path("~/Library/Group Containers/UBF8T346G9.Office/Custom Dictionary")
    ENCODING = "utf-16"
    TYPE_NAME = "mac_office"
