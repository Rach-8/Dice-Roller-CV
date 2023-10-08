from RpiMotorLib import RpiMotorLib
from picamera import PiCamera
import RPi.GPIO as GPIO
import datetime
import time
camera = PiCamera()

i=1
n=10
# Steps:
# Rotate Stepper 180 degrees
# Take a photo and save to a folder (numbered numerically)
# Go to first step

### --- Photo Name and Directory Location ---
# p = 0 # Initial value for number of photos taken
dir_pic = '/home/pi/DiceRoller9000/DicePics/' # Directory to dump photos
# pic_name = '' # File name format - KEEP '%s.jpg'
### --- Photo Name and Directory Location ---

### --- RPi Motor Pin Config ---
direction = 22
step = 23
EN_pin = 24
Sleep_pin = 27
motor = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin, GPIO.OUT)
GPIO.setup(Sleep_pin, GPIO.OUT)
### --- RPi Motor Pin Config

time.sleep(1)

GPIO.output(Sleep_pin, GPIO.HIGH)

def motorspin():
	while True:
		GPIO.output(EN_pin, GPIO.HIGH)
		time.sleep (2)
		camera.capture("/home/pi/DiceRoller9000/Dice_Imgs/dice_pic_"+str(i)+".jpg")
		print("pic clicked"+str(i))
		motor.motor_go(True, "1/4", 100, 0.005, False, 0.05)	
		time.sleep(5)
		motor.motor_go(False, "1/4", 100, 0.005, False, 0.05)
		time.sleep (5)
		GPIO.output(EN_pin, GPIO.HIGH)
	
def motorstop():
	GPIO.output(EN_pin, GPIO.LOW)
		
	
	

try:
	motorspin()
	time.sleep(10000)
	motorstop()

		
		
          
          
          
          
except KeyboardInterrupt:
	GPIO.cleanup()


