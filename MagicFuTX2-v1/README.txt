To run:
>>> export DISPLAY=:0
>>> cd darknet
>>> ./darknet detector demo cfg/coco.data cfg/yolov2-tiny.cfg ../yolov2-tiny.weights ../test_video_3.mp4 -thresh 0.4
Note that if you do not specify video file, then the camera will be used for real-time processing.
