from RpiMotorLib import RpiMotorLib
from picamera import PiCamera
import RPi.GPIO as GPIO
from datetime import date
import time
camera = PiCamera()
import os 

i=1
n=10
# Steps:
# Rotate Stepper 180 degrees
# Take a photo and save to a folder (numbered numerically)
# Go to first step


td = date.today()
cd = td.strftime('%d')
cm = td.strftime('%B')





### --- Photo Name and Directory Location ---
# p = 0 # Initial value for number of photos taken
dir_pic = '/mnt/Dice_pics/D6/Raw/{cm}_{cd}' # Directory to dump photos
# pic_name = '' # File name format - KEEP '%s.jpg'
### --- Photo Name and Directory Location ---



if not os.path.exists(dir_pic):
	os.mkdir(dir_pic)
	print(dir_pic+" created")
else :
	print("directory already exists")



### --- RPi Motor Pin Config ---
direction = 22
step = 23
EN_pin = 24
Sleep_pin = 27
motor = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(Sleep_pin, GPIO.OUT)
### --- RPi Motor Pin Config

time.sleep(1)

GPIO.output(Sleep_pin, GPIO.HIGH)

def motorspin(n):
	while i<n:
		GPIO.output(EN_pin, GPIO.HIGH)
		time.sleep (1)
		camera.capture(dir_pic+"/dice_pic_"+str(i)+".jpg")
		print("pic clicked"+str(i))
		motor.motor_go(True, "full", 100, 0.005, False, 0.05)	
		time.sleep(5)
		motor.motor_go(False, "full", 100, 0.005, False, 0.05)
		time.sleep (1)
		GPIO.output(EN_pin, GPIO.HIGH)
		i=i+1
	
def motorstop():
	GPIO.output(Sleep_pin, GPIO.LOW)
		
	
	

try:
	motorspin()
	motorstop()

		
		
          
          
          
          
except KeyboardInterrupt:
	GPIO.cleanup()


