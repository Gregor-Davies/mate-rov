import XInput
import time
import serial
x = XInput

max_rotation = 1
ser = serial.Serial(port = "COM18", baudrate=9600, timeout=1)

while True:
    state = x.get_state(0)
   
    thumbsticks = x.get_thumb_values(state)
    switches = x.get_button_values(state)
    triggers = x.get_trigger_values(state)

    if switches["A"] == True:
        ser.write(str.encode("001"))
    elif switches["B"] == True:
        ser.write(str.encode("000"))
    elif switches["Y"] == True:
        ser.close()
    
    leftStick = thumbsticks[0][1]*max_rotation

    StickValue = (round(abs(leftStick * 100)))
    #stringValues = (str(StickValue) + " 0 0 0 0 0")
    stringValues = (str(StickValue))
    ser.write(str.encode(stringValues))
    ser.write(str.encode("\r\n"))
    print(stringValues)