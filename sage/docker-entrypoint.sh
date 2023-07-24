#!/bin/bash

env | grep DEBUG

if [ "$DEBUG" == "true" ]; then
    echo -n "Clearing uploads directory ... "
    sudo rm -rf /files/uploads/*.tex
    echo "done."
fi

python3 --version

python3 -u file-watcher.py
