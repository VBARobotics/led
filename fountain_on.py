import RPi.GPIO as GPIO,time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
fountain = 24
GPIO.setup(fountain,GPIO.OUT,initial=GPIO.LOW)
GPIO.output(fountain,GPIO.HIGH)

