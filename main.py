import XInput
x = XInput



#L thumb - rov rotation and movement
#l thumb button - lock for rov
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
max_rotation = 1 #max rotational velocity of the ROV in degrees/s in 1ms
max_elevation = 1 #max amount of m/s that the ROV can go up/down by in 1ms

#Initialisation of variables for the buttons
A = False
Apressed = False
B = False
Bpressed = False
Y = False
Ypressed = False
X = False
Xpressed = False



while True:
    state = x.get_state(0)
   
    thumbsticks = x.get_thumb_values(state)
    switches = x.get_button_values(state)
    triggers = x.get_trigger_values(state)




    rotation = thumbsticks[0][0]*max_rotation #how much to rotate the ROV by every 1ms
    velocity = thumbsticks[0][1] #Velocity of the ROV (Basically controls PMW of the motors for forwards and backwards movement)
    elevation = [triggers[0]*max_elevation triggers[1]*max_elevation] #Up-Down speed. pressing both triggers is frasers issue

    if switches["LEFT_THUMB"] == False:
        lthumbpressed

    if switches["Y"] == False:
        Ypressed = False

    if switches["Y"] == True and Yprepressed == False:
        Y = not Y
        Yprepressed = True

    




    buttons = [X, Y, A, B]
        
    tosend = [velocity, rotation, elevation, buttons, movelock]



    if timeout==1000:
        if x.get_connected() == (False, False, False, False):
            break
        
        else:
            timeout=0


    timeout += 1 