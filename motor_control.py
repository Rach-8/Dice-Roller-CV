import serial
import time
from picamera import PiCamera
from datetime import date
import os

td = date.today()
cd = td.strftime('%d')
cm = td.strftime('%B')
f_nm = f"/mnt/drive/Dice_Rolls/D6/{cd}_{cm}/"

if not os.path.exists(f_nm):
    os.makedirs(f_nm)
    print(f_nm+" created")
else:
    print("already exists")

camera = PiCamera()
ard = serial.Serial(port='/dev/ttyACM0',baudrate=9600,timeout=1)
time.sleep(2)

def step_click(n,path):
    try:
        for i in range(n):
            ard.write(b'+180\n')
            time.sleep(10)
            camera.capture(path+"dice_img_"+str(i)+".jpg")
            time.sleep(2)
            ard.write(b'+180\n')
            time.sleep(6)
    finally:
        ard.close()
        
step_click(3250,f_nm)

