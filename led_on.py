import RPi.GPIO as GPIO,time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
stripled = 22 
redled = 23
yellowled = 24
greenled = 25
GPIO.setup(redled,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(yellowled,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(greenled,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(stripled,GPIO.OUT,initial=GPIO.LOW)
GPIO.output(stripled,GPIO.HIGH)
time.sleep(1)
GPIO.output(redled,GPIO.HIGH)
time.sleep(3)
GPIO.output(yellowled,GPIO.HIGH)
time.sleep(2)
GPIO.output(greenled,GPIO.HIGH)

