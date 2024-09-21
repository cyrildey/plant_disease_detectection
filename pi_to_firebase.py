import RPi.GPIO as GPIO 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
from datetime import datetime
#from picamera import PiCamera
from time import sleep
import os

import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDJu0O_tm2VCB_hqVmmyf3_7LcSgg4ja-M",
  'authDomain': "disease-detection-a1a27.firebaseapp.com",
  'databaseURL': "https://disease-detection-a1a27-default-rtdb.firebaseio.com",
  'projectId': "disease-detection-a1a27",
  'storageBucket': "disease-detection-a1a27.appspot.com",
  'messagingSenderId': "94528270241",
  'appId': "1:94528270241:web:ff049155323d894790a5e0",
  'measurementId': "G-4GV3X5YFDC"
}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

#camera = PiCamera()

while True: 
  try:
    if GPIO.input(10) == GPIO.HIGH:
        print("pushed")
        now = datetime.now()
        dt = now.strftime("%d%m%Y%H:%M:%S")
        name = dt+".jpg"
        #camera.capture(name)
        os.system("rpicam-still -o " + name)
        print(name+" saved")
        storage.child(name).put(name)
        print("Image sent")
        os.remove(name)
        print("File Removed")
        sleep(2)
	
	
  except:
        camera.close()

