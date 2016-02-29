import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)

mylist=[11,12,13,15,16,18,22]

print(time.time())
for i in mylist:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, False)

time.sleep(2)
for j in mylist:
    GPIO.output(j, True)

GPIO.cleanup()
