from xdg import xdg_data_home

from spellsync.dictionary.base import Dictionary


class CommonDictionary(Dictionary):
    """Handle neovim's dictionary.

    Can very easily be re-used for vim, but would have a different path.
    """

    PATH = xdg_data_home() / "spellsync/dictionary"
    TYPE_NAME = "common"

    def add_words(self, dictionary: Dictionary) -> set[str]:
        """Add all the words from the given dictionary to this one."""
        new_words: set[str] = set()
        for word in dictionary:
            if word not in self.words:
                new_words.add(word)
                self.words.add(word)
                self.changes = True
        return new_words

    def write(self, force: bool = False) -> bool:
        if not self.exists():
            self.full_path().parent.mkdir(parents=True, exist_ok=True)
        return super().write()
