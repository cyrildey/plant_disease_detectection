import os
import main
import time
import http.client as httplib
import urllib3 as urllib
from datetime import datetime

key = "R0VJUFRHZTCF2M75"  # Put your API Key here
now = datetime.now()

def predict():
    # Capture video from webcam
    image_number = 0
    image_path = "./captures/" + str(image_number) + ".jpg"
    os.system("rpicam-still -o " + image_path)
    image_number += 1
    # Call the prediction function
    return main.single_prediction(image_path)


def send_info():
    while True:
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp
        index, disease_name = predict()
        
        params = urllib.urlencode({'field1': now, 'field2': index, 'field3': disease_name, 'key':key }) 

        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print temp
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"
        break

if __name__ == "__main__":
        while True:
                send_info()
                time.sleep(60)
 