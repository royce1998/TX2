#!/bin/bash

killall -9 darknet
cd darknet
cp box_coordinate.txt box_coordinate_previousrun.txt
rm box_coordinate.txt
make
./darknet detector demo cfg/coco.data cfg/yolov2-tiny.cfg ../yolov2-tiny.weights -thresh 0.4
cd ../
