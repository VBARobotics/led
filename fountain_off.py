import RPi.GPIO as GPIO,time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
fountain = 24
GPIO.setup(fountain,GPIO.OUT,initial=GPIO.LOW)
GPIO.output(fountain,GPIO.LOW)

