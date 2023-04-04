from picamera import PiCamera
from io import BytesIO
import time

# Create a PiCamera object
camera = PiCamera()

# Set the camera resolution and framerate
camera.resolution = (640, 480)
camera.framerate = 5

# Create a BytesIO object to write the frames to
stream = BytesIO()

# Start recording
camera.start_recording(stream, format='mjpeg')

i=0
prejsni_frame =None

# Loop through the frames
while True:
    # Wait for the next frame
    camera.wait_recording(0.01)
    
    # Read the next frame
    stream.seek(0)
    frame = stream.getvalue()
    
    if prejsni_frame!=frame:
        
        print (i)
        i=i+1

    prejsni_frame = frame
    # Update the stream for the next frame
    stream.seek(0)
    stream.truncate()

    # Check if recording should be stopped
    if i ==1:
        start = time.time()
    if i == 100 :
        break
stop = time.time()

print (stop-start)
# Stop recording
camera.stop_recording()

# Save the video to a file
with open('video.mjpeg', 'ab') as f:
    f.write(stream.getvalue())
