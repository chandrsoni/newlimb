# \2 servos on port 3 and 5

import RPi.GPIO as GPIO
import time
import Tkinter as tk
from calcAngles import *

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
servo1 = GPIO.PWM(3, 50)
servo2 = GPIO.PWM(5, 50)

servo1.start(0)
servo2.start(0)

time.sleep(0.1)
servo1.ChangeDutyCycle(2)
servo2.ChangeDutyCycle(2)
time.sleep(0.1)

root = tk.Tk()
root.geometry("300x600")

def motion(event):
    x, y = event.x, 300 - event.y
    print('x: {},y: {}'.format(x, y))
    a,b = computeAngles(x/150.000000000,y/150.000000000)
    print('a: {},b: {}'.format(a,b))
    servo1.ChangeDutyCycle(7 + (a/18.00))
    servo2.ChangeDutyCycle(2 + (b/18.00))
    time.sleep(0.2)

root.bind('<Motion>', motion)
root.mainloop()


servo1.stop()
servo2.stop()
GPIO.cleanup()