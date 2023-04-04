#import io
#import time
#import picamera
#from PIL import Image
#
#def outputs():
#    stream = io.BytesIO()
#    for i in range(10):
#        # This returns the stream for the camera to capture to
#        yield stream
#        # Once the capture is complete, the loop continues here
#        # (read up on generator functions in Python to understand
#        # the yield statement). Here you could do some processing
#        # on the image...
#        #stream.seek(0)
#        #img = Image.open(stream)
#        # Finally, reset the stream for the next capture
#        stream.seek(0)
#        stream.truncate()
#
#with picamera.PiCamera() as camera:
#    camera.resolution = (640, 480)
#    camera.framerate = 10
#    time.sleep(2)
#    start = time.time()
#    camera.capture_sequence(outputs(), 'jpeg', use_video_port=True)
#    finish = time.time()
#    print('Captured 40 images at %.2ffps' % (10 / (finish - start)))
#
#    print("hope it works")
#
#

import time
import picamera

def premik_servo():
    strat = time.time()
    time.sleep(0.5)
    stop = time.time()
    print(stop-strat)
    print("-------------------")
    
    

with picamera.PiCamera() as camera:

    camera.start_preview()
    camera.start_recording('video.mjpg')
    
    
    time.sleep(2)
    
    

    camera.stop_recording()
    camera.stop_preview()


