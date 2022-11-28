import XInput
x = XInput



#L thumb - rov controls
#l thumb button - lock for rov
#d pad - rotation
#r thumb camera
#back - disable gyro stablization
#RTrigger - Up
#LTrigger - Down
#Y - Light

"""
Buttons output:
{'DPAD_UP': False, 'DPAD_DOWN': False, 'DPAD_LEFT': False, 'DPAD_RIGHT': False, 'START': False, 
'BACK': False, 'LEFT_THUMB': False, 'RIGHT_THUMB': False, 'LEFT_SHOULDER': False, 'RIGHT_SHOULDER': False, 
'A': False, 'B': False, 'X': False, 'Y': False}
"""

timeout = 0 #timer that quits the program if the controller disconects for a certain amount of time
max_rotation = 1 #max amount of degrees that the ROV can rotate in 1ms

#Initialisation of variables for the buttons
A = False
Aprepressed = False
B = False
Bprepressed = False
Y = False
Yprepressed = False
X = False
Xprepressed = False

while True:
    state = x.get_state(0)
   
    thumbsticks = x.get_thumb_values(state)
    buttons = x.get_button_values(state)
    triggers = x.get_trigger_values(state)

    rotation = thumbsticks[0][0]*max_rotation #how much to rotate the ROV by every 1ms
    elevation = [triggers[0], triggers[1]] #Up-Down speed. pressing both triggers is frasers issue

    if buttons["Y"] == False:
        Yprepressed = False

    if buttons["Y"] == True and Yprepressed == False:
        Y = not Y
        Yprepressed = True
        
    print(Y)



    if timeout==1000:
        if x.get_connected() == (False, False, False, False):
            break
        
        else:
            timeout=0


    timeout += 1 