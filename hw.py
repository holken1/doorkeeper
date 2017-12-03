import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT) # green
GPIO.setup(24, GPIO.OUT) # red
GPIO.setup(25, GPIO.IN) # sensor

def set_green(v):
    GPIO.output(23, v)

def set_red(v):
    GPIO.output(24, v)

def is_motion():
    return GPIO.input(25) == 1

GPIO.output(23, False)
GPIO.output(24, False)
