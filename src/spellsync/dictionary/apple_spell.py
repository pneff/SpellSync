import subprocess
from pathlib import Path

from click import echo

from spellsync.dictionary.base import Dictionary


class AppleSpellDictionary(Dictionary):
    """AppleSpell is Mac's system dictionary"""

    PATH = Path("~/Library/Spelling/LocalDictionary")
    TYPE_NAME = "AppleSpell"

    def after_write(self) -> None:
        """Hook invoked after the file has been updated."""
        echo("Stopping AppleSpell to force dictionary update…")
        subprocess.check_call(["killall", "AppleSpell"])
