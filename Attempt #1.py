# Imports go at the top 
from microbit import * 

LED_BRIGHTNESS = 1000 

pin0.write_analog(LED_BRIGHTNESS) 
pin1.write_analog(LED_BRIGHTNESS) 
pin2.write_analog(LED_BRIGHTNESS) 

# Code in a 'while True:' loop repeats forever 
while True: 
    print(display.read_light_level()) 
    if display.read_light_level() >= 100: 
        display.show(Image.SMILE) 
    else: 
        display.show(Image.ANGRY) 
