#!/bin/bash
#sudo bash test_video.sh (No.video)
killall -9 darknet
cd darknet
make
./darknet detector demo cfg/coco.data cfg/yolov2-tiny.cfg ../yolov2-tiny.weights ../test_files/TestVideo"$1".mp4 -thresh 0.2
#move rename here
cd ../
