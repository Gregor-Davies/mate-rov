import XInput
import time
import serial
x = XInput

timeout = 0 #timer that quits the program if the controller disconects for a certain amount of time
max_rotation = 1 #max rotational velocity of the ROV in degrees/s in 1ms
max_elevation = 1 #max amount of m/s that the ROV can go up/down by in 1ms

#Initialisation of variables for the buttons
A = False
Aprepressed = False
B = False
Bpressed = False
Y = False
Yprepressed = False
X = False
Xprepressed = False
lthumb = False
lthumbprepressed = False
back = False
backprepressed = False


ser = serial.Serial(port = "COM4", baudrate=9600, timeout=1)

while True:
    state = x.get_state(0)
    thumbsticks = x.get_thumb_values(state)
    switches = x.get_button_values(state)
    triggers = x.get_trigger_values(state)

    #buttonState = 0
    #if switches["A"] == True:
    #    buttonState = 100
    #elif switches["B"] == True:
    #    buttonState = -100
    if switches["Y"] == True:
        ser.close()
    
    leftStick = thumbsticks[0][1]*max_rotation

    StickValue = (round(leftStick * 100))
    if StickValue < 0:
        stringValues = "-100"
    elif StickValue == 0:
        stringValues = "0"
    else:
        stringValues = "100"
    #stringValues = (str(StickValue) + " 0 0 0 0 0")
    #stringValues = (str(buttonState))
    #stringValues = (str(StickValue))
    ser.write(str.encode(stringValues))
    ser.write(str.encode("\r\n"))
    print(stringValues)
    