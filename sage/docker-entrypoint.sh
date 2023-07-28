#!/bin/bash

env | grep DEBUG

if [ "$DEBUG" == "true" ]; then
    echo -n "Clearing uploads directory ... "
    sudo rm -rf /files/uploads/*.tex
    echo -n "Clearing downloads directory ... "
    sudo rm -rf /files/downloads/*
    echo "done."
fi

sage -python --version

sage -python -u file-watcher.py
