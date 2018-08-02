To run:
>>> export DISPLAY=:0
>>> cd darknet
>>> ./darknet detector demo cfg/coco.data cfg/yolov2-tiny.cfg ../yolov2-tiny.weights ../test_files/test_video_3.mp4 -thresh 0.4
Note that if you do not specify video file, then the camera will be used for real-time processing.

===========================================================

Alternatively, run bash run.sh to run for real-time camera/processing.

===========================================================

Alternatively, run bash run_videos.sh to run the video files inside test_video.

===========================================================

New features for this version:
Multithread processing.
Split 4 core processing (1:3 ratio for fetch and detect).
Output information is also saved in darknet/box_coordinate.txt.
Fixed output information.
Added bash support for pre-recorded video processing.
