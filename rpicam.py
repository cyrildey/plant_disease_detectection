import os
import main
# Capture video from webcam
image_number = 0
cap = os.system("rpicam-still -o ./captures/" + str(image_number) + "jpg")
image_number += 1
# Call the prediction function
main.single_prediction(cap)
