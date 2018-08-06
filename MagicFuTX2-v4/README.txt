
To run:
>>> export DISPLAY=:0
>>> cd darknet2
>>> ./darknet detector demo cfg/coco.data cfg/yolov2-tiny.cfg ../yolov2-tiny.weights ../test_files/test_video_3.mp4 -thresh 0.4

Note: Use the darknet directory for real-time processing and darknet2 to process pre-recorded videos.

===========================================================

Alternatively, run bash run.sh to run for real-time camera/processing.

===========================================================

New features for this version:
Multithread processing.
Split 4 core processing (1:3 ratio for fetch and detect).
Output information is also saved in darknet/box_coordinate.txt.
Fixed output information.
RUNS 3x FASTER than VERSION 2!!!
