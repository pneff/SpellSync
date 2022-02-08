import re
from pathlib import Path

from spellsync.dictionary.base import Dictionary


class AspellDictionary(Dictionary):
    """Handle custom dictionary for aspell."""

    PATH = Path("~/.aspell.en.pws")
    TYPE_NAME = "aspell"

    @classmethod
    def instantiate(cls) -> bool:
        """Always create this file, even if the dictionary file isn't there yet."""
        return True

    def read(self) -> None:
        with self._open_file("r") as f:
            # Skip the first line
            first_line = f.readline()
            assert first_line.startswith("personal_ws")

            for line in f:
                self.words.add(line.strip())

    def write(self, force: bool = False) -> bool:
        if force or self.changes:
            with self._open_file("w") as f:
                f.write("personal_ws-1.1 en 0 utf-8\n")
                for word in sorted(self.words):
                    if self._is_valid_word(word):
                        f.write(word)
                        f.write("\n")
            return True
        else:
            return False

    def _is_valid_word(self, word: str) -> bool:
        """Aspell does not allow all characters in its word.

        I could not yet find any official documentation, so the following list
        is based on exceptions encountered when using Aspell.
        """
        return not bool(re.search("[.]", word))
