#!/bin/bash
FILE=$1
UPLOAD_DIR=$2

sudo chown sage:sage "${UPLOAD_DIR}/${FILE}.tex"

TEMPDIR=$(mktemp -d)
cd $TEMPDIR
sudo mv "${UPLOAD_DIR}/${FILE}.tex" ./

pdflatex "${FILE}.tex" > /dev/null 2>&1
sage "${FILE}.sagetex.sage" > /dev/null 2>&1
pdflatex "${FILE}.tex" > /dev/null 2>&1

sudo mkdir /files/downloads
sudo tar zcvf /files/downloads/${FILE}.tgz ${FILE}.* > /dev/null 2>&1

tar ztvf "/files/downloads/${FILE}.tgz"

sudo mv * /files/downloads/

cd ~/
rm -rf $TEMPDIR

exit 0
