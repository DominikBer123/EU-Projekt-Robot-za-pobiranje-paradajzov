frame = 1
kot=0
smer_vrstenja = 0 # 0 -> prošteva ; 1-> odšteva 

def Servo_motor():
    global kot, frame, smer_vrstenja
    
    
    if smer_vrstenja == 0:
        #kit.servo[0].angle = kot
        print('frame ='+ str(frame) + '  kot = ' + str(kot))
        kot=kot+20
        if kot == 200:
            smer_vrstenja = 1
        
    elif(smer_vrstenja == 1):
        kot = kot - 20
        #kit.servo[0].angle = kot
        print('frame ='+ str(frame) + '  kot = ' + str(kot))
        if kot == 0:
            smer_vrstenja = 0
    frame=frame+1

for i in range(100):
    Servo_motor()

