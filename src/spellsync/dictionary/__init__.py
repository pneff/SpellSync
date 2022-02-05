from typing import List, Type

from spellsync.dictionary.base import Dictionary
from spellsync.dictionary.mac_office import MacOfficeDictionary
from spellsync.dictionary.neovim import NeovimDictionary

all_dictionary_classes: List[Type[Dictionary]] = [MacOfficeDictionary, NeovimDictionary]
