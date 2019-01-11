import RPi.GPIO as GPIO,time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for i in range (22,26):
   ledpin = i
   print ledpin,' off'
   time.sleep(1)
   GPIO.setup(ledpin,GPIO.OUT,initial=GPIO.LOW)
   GPIO.output(ledpin,GPIO.LOW)

