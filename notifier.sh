#!/bin/bash

LASTFILE=last.txt
LISTFILE=wandbox-compilers.txt
USERNAME=srz-zumix
PROJECT=wandbox-news
wandbox --retry 3 compiler > $LISTFILE
if [ $? -ne 0 ]
then
	rm -rf $LISTFILE
	exit 1
fi

curl -sL -o $LASTFILE https://ci.appveyor.com/api/projects/$USERNAME/$PROJECT/artifacts/$LISTFILE?branch=master
#cat $LASTFILE

python wandbox-compilerlist-diff.py $LASTFILE $LISTFILE > diff.txt
