#!/bin/bash
export url=$1
export outputpath=$2

wget $url -O image.png
python hello.py image.png $outputpath
cat $outputpath
