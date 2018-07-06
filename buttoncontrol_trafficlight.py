from gpiozero import CPUTemperature, LED, Button
from signal import pause
import RPi.GPIO as GPIO
import time, sys
from time import sleep, strftime, time
import matplotlib.pyplot as plt

plt.ion()
x1 = []
y1 = []
x2 = []
y2 = []

color = 1
redled = LED(18)
button = Button(17)
greenled = LED(27)

def redOn():
    
    #button.when_pressed = redled.on
    redled.on()
    t=10
    """ while t > 0:
        print(t)
        redled.on()
        sleep(1)
        redled.off()   
        sleep(1)
        t -= 1"""

def greenOn():
    greenled.on()
    """while greenled.on == True:
        with open("led_color.csv","a") as log:
            log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),0))
            sleep(1)
    #log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),green))"""
    t=15
    while t > 0:
        print(t)
        greenled.on()
        sleep(1)
        t -= 1
    if t==0 :
        greenled.off()
        redled.on()

    
def yellowOn():
   
    
    greenled.on()
    redled.on()
    greenled.off()
    redled.off()
  

def main():
    print("Press button twice to cross street")
    redled.on()
    color = 1
    while True:
    
        button.wait_for_press(3)
        if button.is_pressed == True :
        
            color = 0 #green               
            redled.off()
            greenOn()
        else:
            print("Do you want to turn it off? y/n")
            cmd = input("-->")
            if cmd == "y":
                redled.off()
                greenled.off()
                return
               
            else:
                redled.on()
                color = 1 #red
           
                   
                print("Press the button to cross.")
                button.wait_for_press(60)
    return

main()
