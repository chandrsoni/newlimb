# \2 servos on port 3 and 5

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
servo1 = GPIO.PWM(3, 50)
servo2 = GPIO.PWM(5, 50)

servo1.start(0)
servo2.start(0)

print("waiting for 2 seconds")
time.sleep(2)

duty = 2

while duty < 13:
    servo1.ChangeDutyCycle(duty)
    servo2.ChangeDutyCycle(duty)
    time.sleep(0.3)
    servo1.ChangeDutyCycle(0)
    servo2.ChangeDutyCycle(0)
    time.sleep(0.7)
    duty = duty + 1

servo1.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(2)
time.sleep(1)

servo1.stop()
servo2.stop()
GPIO.cleanup()
print("Goodbye")