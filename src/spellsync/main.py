from typing import List

import click
from click import echo

from spellsync.dictionary import all_dictionary_classes
from spellsync.dictionary.base import Dictionary
from spellsync.dictionary.common import CommonDictionary


def find_dictionaries() -> List[Dictionary]:
    """Return all dictionaries that can be found on the system."""
    ret: List[Dictionary] = []

    for DictionaryClass in all_dictionary_classes:
        if DictionaryClass.is_present():
            ret.append(DictionaryClass())

    return ret


@click.command()
@click.pass_context
def main(ctx: click.Context) -> None:
    """Just an initial test."""
    dictionaries = find_dictionaries()
    if not dictionaries:
        echo("No dictionary found.")
        ctx.exit(1)

    echo(f"Found {len(dictionaries)} dictionaries:")
    for dictionary in dictionaries:
        echo(f"  - {dictionary}")

    common = CommonDictionary()
    for dictionary in dictionaries:
        common.add_words(dictionary)
    echo(f"Merged into common dictionary - {len(common)} words total")
