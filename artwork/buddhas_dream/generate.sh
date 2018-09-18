#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "Please provide buddha's age and duration of dream as input (Eg: ./fractal-buddha.sh 500 10)" 
    exit
fi

cd ../../fractal_generators/buddhabrot
gcc buddha.c -lm -o buddha
count=1
while [ $count -le $2 ] 
do
 timeout $1 ./buddha
 python2 draw.py
 mv buddha.png buddha_${count}.png
 ((count++))
done
rm -rf buddha r.txt g.txt b.txt 
mv buddha_1.png buddha_01.png && mv buddha_2.png buddha_02.png && mv buddha_3.png buddha_03.png && mv buddha_4.png buddha_04.png && mv buddha_5.png buddha_05.png && mv buddha_6.png buddha_06.png && mv buddha_7.png buddha_07.png && mv buddha_8.png buddha_08.png && mv buddha_9.png buddha_09.png
convert -delay 5 -loop 0 *.png buddha.gif
mv buddha.gif ../../artwork/buddhas_dream/
rm *.png
cd - 
