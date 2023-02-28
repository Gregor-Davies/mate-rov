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


while True:
    state = x.get_state(0)
   
    thumbsticks = x.get_thumb_values(state)
    switches = x.get_button_values(state)
    triggers = x.get_trigger_values(state)




    rotation = thumbsticks[0][0]*max_rotation #how much to rotate the ROV by every 1ms
    velocity = thumbsticks[0][1] #Velocity of the ROV (Basically controls PMW of the motors for forwards and backwards movement)
    elevation = [triggers[0]*max_elevation triggers[1]*max_elevation] #Up-Down speed. pressing both triggers is frasers issue
    camera = [thumbsticks[1][0], thumbsticks[1][1]] #This is camera movement

    if switches["LEFT_THUMB"] == False:
        lthumbprepressed = False

    if switches["LEFT_THUMB"] == True and lthumbprepressed == False:
        lthumb = not lthumb #If true, lock rotation and velocity for ROV
        lthumbprepressed = True


    if switches["Y"] == False:
        Yprepressed = False

    if switches["Y"] == True and Yprepressed == False:
        Y = not Y #If true, this turns on flashlight
        Yprepressed = True

    if switches["back"] == False:
        backprepressed = False

    if switches["back"] == True and backprepressed == False:
        back = not back #If true then this should disable gyro 
        backprepressed = True





    buttons = [X, Y, A, B, lthumb]
        
    tosend = [velocity, rotation, elevation, buttons, camera]



    if timeout==1000:
        if x.get_connected() == (False, False, False, False):
            break
        
        else:
            timeout=0


    timeout += 1 