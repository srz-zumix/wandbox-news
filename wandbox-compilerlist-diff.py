#!/usr/bin/env python
#
# wandbox-compilerlist-diff.py
#

import sys

if __name__ == '__main__':
    lastfile = 'last.txt'
    listfile = 'wandbox-compilers.txt'
    if len(sys.argv) > 2:
        lastfile = sys.argv[1]
        listfile = sys.argv[2]
    old_list = []
    new_list = []
    with open(lastfile) as fp:
        for line in fp:
            old_list.append(line.strip())
    with open(listfile) as fp:
        for line in fp:
            new_list.append(line.strip())
    deleted_list = [x for x in old_list if x not in new_list]
    added_list = [x for x in new_list if x not in old_list]

    for d in added_list:
        print('NEW!: ' + d)
    for d in deleted_list:
        print('Deleted: ' + d)
    if deleted_list or added_list:
        sys.exit(1)
