# Introduction

This utility synchronises spelling dictionaries from various tools with each
other. This way the words that have been trained on MS Office are also
correctly checked in vim or Firefox. And vice versa of course.

# Supported tools

The initial supported tools are:

* AppleSpell (Mac OS built-in spelling)
* Microsoft Office (Mac)
* Mozilla Firefox (Mac)
* aspell
* neovim - adjusting for vim would be trivial though

# Process

SpellSync accomplishes this work by reading all the stored words from all the
dictionaries. It stores that dictionary in a central location. From there the
individual app dictionaries are updated with the merged list.

# Installation

SpellSync is created in Python and published on Python's PyPI. Installation in
most cases is accomplished with the following command:

    pip install spellsync

# Usage

Once set up, you can do a dry-run of `spellsync` with the following command:

    spellsync -n

This will show how large the common dictionary will become, but no files are
written.

To execute the sync in live mode, run without the `-n` option:

    spellsync


## Recovering from Errors

By default a backup of all spelling files is created in the `spellsync` folder
inside the XDG state home (default location is `~/.local/state/spellsync`). So
if anything goes awry, you can use the backup files from there. The path to the
dictionary files that are modified is output when the command is run, which
should aid in finding out where the files would have to be moved back to.

Note that the backup folder is not cleaned out or rotated. So if you run the
script regularly, the folder may grow too large. You can then either manually
clear out old backup files (`tmpwatch` may be helpful here) or you can disable
the backup altogether:

    spellsync --no-backup
