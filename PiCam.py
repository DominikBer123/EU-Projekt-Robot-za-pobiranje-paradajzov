

##===================================================================================##
##======================================DELA H264====================================##
##===================================================================================##

import time
from picamera2 import Picamera2
from picamera2.encoders import MJPEGEncoder
from adafruit_servokit import ServoKit

kit = ServoKit(channels=8)


i = 0

def ola(data):
    global i
    i=i+1
    print(i)
    if i <=180:
        kit.servo[0].angle = i
    else:
        i = 0


kit.servo[0].angle = 0
time.sleep(1)

picam2 = Picamera2()
picam2.post_callback =ola
video_config = picam2.create_video_configuration()

picam2.sensor_mode = 4
picam2.framerate = 30

picam2.configure(video_config)

encoder = MJPEGEncoder()

picam2.start_recording(encoder, 'test')
time.sleep(5)
picam2.stop_recording()




