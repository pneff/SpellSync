import datetime
import shutil
from pathlib import Path
from typing import Generator

from xdg import xdg_state_home


class Dictionary:
    """Base class for all dictionaries."""

    PATH: Path
    TYPE_NAME: str
    ENCODING = "utf-8"

    words: set[str]
    changes = False

    def __init__(self) -> None:
        self.words = set()

        if self.exists():
            with self.full_path().open("r", encoding=self.ENCODING) as f:
                for line in f:
                    self.words.add(line.strip())

    @classmethod
    def full_path(cls) -> Path:
        return cls.PATH.expanduser()

    @classmethod
    def exists(cls) -> bool:
        """Return True if a dictionary was found on the system."""
        return cls.full_path().exists()

    def write(self, force: bool = False) -> bool:
        if force or self.changes:
            with self.full_path().open("w", encoding=self.ENCODING) as f:
                for word in sorted(self.words):
                    f.write(word)
                    f.write("\n")
            return True
        else:
            return False

    def backup(self) -> Path:
        """Create a backup of the file."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
        backup_folder = xdg_state_home() / f"spellsync/{timestamp}"
        backup_folder.mkdir(parents=True, exist_ok=True)
        backup_file = backup_folder / self.TYPE_NAME
        shutil.copyfile(self.full_path(), backup_file)
        return backup_file

    def __iter__(self) -> Generator[str, None, None]:
        yield from self.words

    def __len__(self) -> int:
        return len(self.words)

    def replace_words(self, dictionary: "Dictionary") -> None:
        """Replace the words in this dictionary with the words from the other dictionary."""
        new_words = set()
        for word in dictionary:
            new_words.add(word)

        if new_words != self.words:
            self.changes = True
            self.words = new_words
