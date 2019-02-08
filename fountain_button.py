import RPi.GPIO as GPIO
import time
GPIO.cleanup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
fountain = 24
button = 25
GPIO.setup(fountain,GPIO.OUT,initial=GPIO.HIGH)
GPIO.setup(button,GPIO.IN,GPIO.PUD_UP)

while GPIO.input(25):
    pass
print("Button Pushed")
GPIO.output(fountain,GPIO.LOW)

