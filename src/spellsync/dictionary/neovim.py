from xdg import xdg_config_home

from spellsync.dictionary.base import Dictionary


class NeovimDictionary(Dictionary):
    """Handle neovim's dictionary.

    Can very easily be re-used for vim, but would have a different path.
    """

    PATH = xdg_config_home() / "nvim/spell/en.utf-8.add"
    TYPE_NAME = "nvim"
