from picamera2 import Picamera2

# Initialize the camera
camera = Picamera2()

def aaaa(data):
    print("aaaaa")

camera.pre_callback =aaaa
# Capture a video at the maximum frame rate for 10 seconds
camera.start_recording('video.h264')
camera.wait_recording(2)
camera.stop_recording()