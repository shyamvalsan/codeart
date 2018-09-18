#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "Please provide buddha's age as input (Eg: ./fractal-buddha.sh 500)" 
    exit
fi

cd buddhabrot
gcc buddha.c -lm -o buddha
timeout $1 ./buddha
python2 draw.py
rm -rf buddha r.txt g.txt b.txt 
cd - 
