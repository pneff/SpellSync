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
        if DictionaryClass.exists():
            ret.append(DictionaryClass())

    return ret


@click.command()
@click.option("--no-op", "-n", is_flag=True, help="Do not write any files.")
@click.option("--backup/--no-backup", help="Write backups.", default=True)
@click.pass_context
def main(ctx: click.Context, no_op: bool, backup: bool) -> None:
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

    if not no_op:
        if backup and common.exists():
            common.backup()
        echo(f"Storing common dictionary in {common.full_path()}")
        if not common.write():
            echo(f"  - No changes")

    for dictionary in dictionaries:
        dictionary.replace_words(common)
        if not no_op:
            if backup:
                backup_file = dictionary.backup()
                echo(f"Backed up {dictionary.TYPE_NAME} to {backup_file}")
            if not dictionary.write():
                echo(f"No changes for {dictionary.TYPE_NAME}")
