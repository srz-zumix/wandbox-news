#!/bin/bash

LISTFILE=wandbox-compilers.txt
python wandbox-listup-compiler.py > $LISTFILE
#curl https://circleci.com/api/v1.1/project/github/circleci/wandbox-news/$CIRCLE_BUILD_NUM/artifacts/0/$CIRCLE_ARTIFACTS/$LISTFILE

