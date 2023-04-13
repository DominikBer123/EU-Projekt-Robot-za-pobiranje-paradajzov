########--------uporabljene knjižnice----------
import time
from picamera2 import Picamera2 #sudo pip inszall picamera2 == 0.3.8
from picamera2.encoders import JpegEncoder
from adafruit_servokit import ServoKit

#Uporabljeni kanal za servo motor
kit = ServoKit(channels=8)
kit.servo[0].set_pulse_width_range(200, 2800)

strat1=time.time()
stop2=time.time()
strat2=time.time()
stop1=time.time()

#counter
frame = 0
kot=0
smer_vrstenja = 0 # 0 -> prošteva ; 1-> odšteva 

def Servo_motor(data):
    global kot, frame, smer_vrstenja
    global strat2,strat1,stop1,stop2
    strat=time.time()
    
    
    if smer_vrstenja == 0:
        kit.servo[0].angle = kot
        print('frame ='+ str(frame) + '  kot = ' + str(kot))
        kot=kot+20
        if kot == 200:
            strat1=time.time()
            stop2=time.time()
            print(stop2-strat2)
            
            smer_vrstenja = 1
        
    elif(smer_vrstenja == 1):
        kot = kot - 20
        kit.servo[0].angle = kot
        print('frame ='+ str(frame) + '  kot = ' + str(kot))
        if kot == 0:
            strat2=time.time()
            stop1=time.time()
            print(stop1-strat1)
            smer_vrstenja = 0
    
    frame=frame+1





kit.servo[0].angle = 0
time.sleep(2)


picam2 = Picamera2()
video_config = picam2.create_video_configuration(main={"size": (1920, 1080)},controls={"FrameDurationLimits": (100000, 100000)}) 
picam2.configure(video_config)

picam2.pre_callback =Servo_motor

picam2.start_preview()
encoder = JpegEncoder(q=70)

picam2.start_recording(encoder, 'test.mjpeg')
time.sleep(30)
picam2.stop_recording()