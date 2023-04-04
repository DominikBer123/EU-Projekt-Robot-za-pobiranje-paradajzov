from picamera import PiCamera
from io import BytesIO

# Create a PiCamera object
camera = PiCamera()

# Set the camera resolution and framerate
camera.resolution = (640, 480)
camera.framerate = 10

# Create a BytesIO object to write the frames to
stream = BytesIO()

# Start recording
camera.start_recording('vid.mjpg', format='mjpeg')
i=0
prejsni_frame=None
# Loop through the frames
while True:
    # Wait for the next frame
    camera.wait_recording(0.01)

    # Read the next frame
    stream.seek(0)
    frame = stream.getvalue()
    
    # TODO: Compare the current frame to the previous frame and do something if they are different
    if prejsni_frame!=frame:
        print (i)
        i=i+1
    # Display the current framerate on the video
    
    
    prejsni_frame = frame
    # Update the stream for the next frame
    stream.seek(0)
    stream.truncate()
    if i == 100 :
        break

# Stop recording
camera.stop_recording()
