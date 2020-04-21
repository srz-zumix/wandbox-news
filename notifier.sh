#!/bin/bash

python --version

LASTFILE=last.txt
LISTFILE=wandbox-compilers.txt
USERNAME=srz-zumix
PROJECT=wandbox-news
python wandbox-listup-compiler.py > $LISTFILE
if [ $? -ne 0 ]
then
	rm -rf $LISTFILE
	exit 1
fi

curl -sL -o $LASTFILE https://ci.appveyor.com/api/projects/$USERNAME/$PROJECT/artifacts/$LISTFILE?branch=master
#cat $LASTFILE

python wandbox-compilerlist-diff.py $LASTFILE $LISTFILE > diff.txt
