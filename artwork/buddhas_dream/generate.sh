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
cp buddha_49.png buddha_51.png && cp buddha_48.png buddha_52.png && cp buddha_47.png buddha_53.png && cp buddha_46.png buddha_54.png && cp buddha_45.png buddha_55.png && cp buddha_44.png buddha_56.png && cp buddha_43.png buddha_57.png && cp buddha_42.png buddha_58.png && cp buddha_41.png buddha_59.png && cp buddha_40.png buddha_60.png && cp buddha_39.png buddha_61.png && cp buddha_38.png buddha_62.png && cp buddha_37.png buddha_63.png && cp buddha_36.png buddha_64.png && cp buddha_35.png buddha_65.png && cp buddha_34.png buddha_66.png && cp buddha_33.png buddha_67.png && cp buddha_32.png buddha_68.png && cp buddha_31.png buddha_69.png && cp buddha_30.png buddha_70.png && cp buddha_29.png buddha_71.png && cp buddha_28.png buddha_72.png && cp buddha_27.png buddha_73.png && cp buddha_26.png buddha_74.png && cp buddha_25.png buddha_75.png && cp buddha_24.png buddha_76.png && cp buddha_23.png buddha_77.png && cp buddha_22.png buddha_78.png && cp buddha_21.png buddha_79.png && cp buddha_20.png buddha_80.png && cp buddha_19.png buddha_81.png && cp buddha_18.png buddha_82.png && cp buddha_17.png buddha_83.png && cp buddha_16.png buddha_84.png && cp buddha_15.png buddha_85.png && cp buddha_14.png buddha_86.png && cp buddha_13.png buddha_87.png && cp buddha_12.png buddha_88.png && cp buddha_11.png buddha_89.png && cp buddha_10.png buddha_90.png && cp buddha_09.png buddha_91.png && cp buddha_08.png buddha_92.png && cp buddha_07.png buddha_93.png && cp buddha_06.png buddha_94.png && cp buddha_05.png buddha_95.png && cp buddha_04.png buddha_96.png && cp buddha_03.png buddha_97.png && cp buddha_02.png buddha_98.png && cp buddha_02.png buddha_99.png  
mv buddha.gif ../../artwork/buddhas_dream/
#rm *.png
cd - 
