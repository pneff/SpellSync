# Introduction

This utility synchronises spelling dictionaries from various tools with each
other. This way the words that have been trained on MS Office are also
correctly checked in vim or Firefox. And vice versa of course.

# Supported tools

The initial supported tools are:

* Microsoft Office (Mac)
* Mozilla Firefox (Mac)
* neovim - adjusting for vim would be trivial though
* AppleSpell (Mac OS built-in spelling)

# Process

SpellSync accomplishes this work by reading all the stored words from all the
dictionaries. It stores that dictionary in a central location. From there the
individual app dictionaries are updated with the merged list.
