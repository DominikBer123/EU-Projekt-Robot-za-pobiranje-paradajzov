

##===================================================================================##
##======================================DELA H264====================================##
##===================================================================================##

import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from adafruit_servokit import ServoKit

kit = ServoKit(channels=8)


i = 0

def ola(data):
    global i
    i=i+36
    print(i)
    if i <=180:
        kit.servo[0].angle = i
    else:
        i = 0



picam2 = Picamera2()
picam2.framerate = 10
picam2.pre_callback =ola
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

encoder = H264Encoder(10000000)

picam2.start_recording(encoder, 'test.h264')
time.sleep(10)
picam2.stop_recording()




