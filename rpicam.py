import os
import main
import time

def predict():
    # Capture video from webcam
    image_number = 0
    image_path = "./captures/" + str(image_number) + ".jpg"
    os.system("rpicam-still -o " + image_path)
    image_number += 1
    # Call the prediction function
    main.single_prediction(image_path)

while True:
    predict()
    time.sleep(1)
