# !/bin/python

import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)   #Change GPIO PIN If Needed
def Shutdown(channel):
    print("Reboot")
    time.sleep(3)
    os.system("sudo reboot")   #reboot/shutdown command

GPIO.add_event_detect(26, GPIO.FALLING, callback=Shutdown, bouncetime=2000)   #Change GPIO PIN If Needed

while 1:

    time.sleep(1)
