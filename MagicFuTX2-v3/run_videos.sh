#!/bin/bash

killall -9 darknet
cd darknet
cp box_coordinate.txt box_coordinate_previousrun.txt
rm box_coordinate.txt
make
for f in ../test_files/*.avi; do
    ffmpeg -i ../test_files/"$f" ../test_files/"$f".mp4
    rm "$f"
done
for g in ../test_files/*.mp4; do
    ./darknet detector demo cfg/coco.data cfg/yolov2-tiny.cfg ../yolov2-tiny.weights ../test_files/"$g" -thresh 0.4
done
cd ../
