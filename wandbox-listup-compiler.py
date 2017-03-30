#!/usr/bin/env python
#
# wandbox-listup-compiler.py
#

import json

from wandbox import Wandbox


if __name__ == '__main__':
    w = Wandbox()
    r = w.get_compiler_list()
    for d in r:
        print('{0}: {1}'.format(d['language'], d['name']))
