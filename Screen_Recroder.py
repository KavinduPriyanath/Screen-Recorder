import pyautogui
import cv2
import numpy as np


#Create a VideoWriter Object
filename = "Recording.avi"
resolution = pyautogui.size()
fps = 15.0
codec = cv2.VideoWriter_fourcc(*"XVID")

output = cv2.VideoWriter(filename, codec, fps, resolution)

#The main infinite loop
while True:
	img = pyautogui.screenshot()

	frame = np.array(img)

	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# Write it to the output file
	output.write(frame)

output.release()

cv2.destroyAllWindows()
