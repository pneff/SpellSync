from xdg import xdg_data_home

from spellsync.dictionary.base import Dictionary


class CommonDictionary(Dictionary):
    """Handle neovim's dictionary.

    Can very easily be re-used for vim, but would have a different path.
    """

    PATH = xdg_data_home() / "spellsync/dictionary"

    def __init__(self) -> None:
        super().__init__()
        if self.is_present():
            with self.PATH.open() as f:
                for line in f:
                    self.words.add(line.strip())

    @staticmethod
    def is_present() -> bool:
        """Return True if a dictionary was found on the system."""
        return CommonDictionary.PATH.exists()

    def add_words(self, dictionary: Dictionary) -> None:
        for word in dictionary:
            self.words.add(word)
