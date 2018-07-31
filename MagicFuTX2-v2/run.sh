#!/bin/bash

killall -9 darknet
cd darknet
./darknet detector demo cfg/coco.data cfg/yolov2-tiny.cfg ../yolov2-tiny.weights -thresh 0.4
cd ../
