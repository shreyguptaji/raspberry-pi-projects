from bluedot import BlueDot
from gpiozero import LED
import RPi.GPIO as GPIO

bd = BlueDot()
#bd.wait_for_press()

red = 13
green = 15


def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(red, GPIO.OUT)
	GPIO.setup(green, GPIO.OUT)
	GPIO.output(red, GPIO.LOW)
	GPIO.output(green, GPIO.LOW)


def loop():
    
    while True:
        if bd.wait_for_press(5) == True:
            GPIO.output(red, GPIO.HIGH)
            GPIO.output(green, GPIO.LOW)

        else:
            GPIO.output(green, GPIO.HIGH)
            GPIO.output(red, GPIO.LOW)

 
def destroy():
	GPIO.output(red, GPIO.HIGH)
	GPIO.output(green, GPIO.HIGH) 
	GPIO.cleanup()                     # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()

        
