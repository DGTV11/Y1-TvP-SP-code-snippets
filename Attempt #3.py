import os  

from microbit import * 
import music, machine

# FUNCTIONS
beep = lambda: music.play(['c'])  
yay_beep = lambda: music.play(['d'])  
uh_oh_beep = lambda: music.play(['f'])  

def calibrate() -> int:  
    '''
    Gets the average nominal light level.  
    To ensure reliable results, place the bin in its operating location,   
    ensure that the laser is turned on   
    and pointed towards the top-center of the LED display.  
    When you are ready, press the gold logo to begin calibration.  
    '''
  
    yay_beep()
  
    while not pin_logo.is_touched(): # Blocks  
        # print(display.read_light_level())  
        if button_b.is_pressed(): #Debug 
            display.show(display.read_light_level()) 
            display.clear() 

    ## More memory-efficient way to get average  
    ave_nominal_light_level = 0  
    for i in range(100):  
        if i%20==0:  
            beep()  

        ave_nominal_light_level += display.read_light_level()  
    ave_nominal_light_level //= 100  

    # Send feedback to user and return nominal light level
    yay_beep() 
  
    return ave_nominal_light_level  

# CONSTANTS  
MIN_DIFFERENCE = 50  
AVE_NOMINAL_LIGHT_LEVEL_FILENAME = 'ave_nominal_light_level' 

# CALIBRATE ON FIRST STARTUP  
try: # Here, it's better to ask for forgiveness than permission (because simplicity rules)  
    with open(AVE_NOMINAL_LIGHT_LEVEL_FILENAME, 'r') as f: # Attempting to read from persistent storage  
        ave_nominal_light_level = int(f.read())  
    yay_beep()  
except: # Whoops! Persistent storage doesn't even EXIST!  
    ave_nominal_light_level = calibrate()  
    with open(AVE_NOMINAL_LIGHT_LEVEL_FILENAME, 'w') as f: # Writing to persistent storage  
        f.write(str(ave_nominal_light_level))  

# MAIN LOOP  
while True:    
    light_level = display.read_light_level() 
    # print(light_level)
    if light_level < ave_nominal_light_level-MIN_DIFFERENCE: # If light level is more than MIN_DIFFERENCE below ave_nominal_light_level,  
        uh_oh_beep() # Do annoying beep because we couldn't account for the tinker kit in our design in time  
    if pin_logo.is_touched(): # Allows user to re-calibrate if need be  
        ave_nominal_light_level = calibrate()  
        with open(AVE_NOMINAL_LIGHT_LEVEL_FILENAME, 'w') as f: # I seriously hope you can infer what this does  
            f.write(str(ave_nominal_light_level))  
    elif button_a.is_pressed(): # Guess what this does  
        os.remove(AVE_NOMINAL_LIGHT_LEVEL_FILENAME)  
        machine.reset() # triggers restart  
    elif button_b.is_pressed(): #Debug 
        display.show(light_level) 
        display.clear() 
