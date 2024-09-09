from microbit import *  

THRESHOLD = 100 # TODO: get threshold through the use of neural network/linear regression  

while True:  
    light_level = display.read_light_level()  
    print(light_level) 

    if light_level >= THRESHOLD:
        display.show(Image.SMILE) 
    else:
        display.show(Image.ANGRY)
