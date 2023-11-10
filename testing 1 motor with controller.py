import XInput
import time
import serial
x = XInput

max_rotation = 1
ser = serial.Serial(port = "COM22", baudrate=9600, timeout=5)

while True:
    state = x.get_state(0)
   
    thumbsticks = x.get_thumb_values(state)
    switches = x.get_button_values(state)
    triggers = x.get_trigger_values(state)

    leftStick = thumbsticks[0][1]*max_rotation

    time.sleep(0.5)
    StickValue = (round(abs(leftStick * 100)))
    stringValues = (str(StickValue) + " 0 0 0 0 0")
    time.sleep(5)
    ser.write(bytes(stringValues, 'utf-8'))
    response = serial.readline()
    print(response)
