#!/bin/bash

set -e

LASTFILE=last.txt
LISTFILE=wandbox-compilers.txt
USERNAME=srz-zumix
PROJECT=wandbox-news
python wandbox-listup-compiler.py > $LISTFILE

curl -sL -o $LASTFILE https://ci.appveyor.com/api/projects/$USERNAME/$PROJECT/artifacts/$LISTFILE?branch=master
#cat $LASTFILE

python wandbox-compilerlist-diff.py $LASTFILE $LISTFILE
