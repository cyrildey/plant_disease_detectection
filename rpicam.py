import os
import main
import time
import http.client as httplib
import urllib3 as urllib
from datetime import datetime
import requests
import pyrebase

print('importations done')

key = "R0VJUFRHZTCF2M75"  # Put your API Key here



# put the firebase comfig here
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
print('firebase connected') 


def predict():
    # Capture video from webcam
    os.system("rpicam-still -o " + image_path)
    # Call the prediction function
    return main.single_prediction(image_path)


def send_info():
        
        index, disease_name,disease_description = predict()
        disease_name = str(disease_name)
        index = str(index)

        #send data to firebase
        storage.child(image_name).put(image_path)
        print('image sent to firebase')

        # send data to thinkspeak
        url = 'https://api.thingspeak.com/update'
        data = {"field1": image_name, "field2": index, "field3": disease_name, "field4":disease_description, "key":key }
        response = requests.post(url, json=data)
        print('This is the result from thingspeak')
        print(response.json())


if __name__ == "__main__":
        while True:
                now = datetime.now()
                dt = now.strftime("%d%m%Y%H:%M:%S")
                image_name = dt+".jpg"
                image_path = "./captures/" + image_name
                send_info()
                time.sleep(60)
 