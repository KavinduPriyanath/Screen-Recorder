# Screen-Recorder
A simple Screen Recorder made using Numpy, OpenCV and Pyautogui Python libraries.<br/>
How it happens?

First create a VideoWriter Object using opencv.
Necessary parameters in VideoWriter Object,
	1) Output filename
	2) Resolution
			-Here the correct Screen Size is needed or writing to file won't work. Can use pyautogui.size() to get the size of the primary monitor
	3) FPS
	4) Video Codec (XVID, MJPG, X264)



Inside the infinite loop,
	1) Capture a screenshot using pyautogui
	2) Convert that screenshot to a numpy array
	3) Write it to the output file using the VideoWriter Object

cvtColor() is used for Colour Space Conversion (To RGB) because OpenCV use BGR by default.

img = pyautogui.screenshot(region=(0,0,200,200)) can also be used to capture only a part of the screen but the would need to change the screen resolution too. Parameters are (top, left, width, height).In this case, 
	resolution = (200,200)

Finally we close the VideoWriter using ouput.release() and then destroy all opened windows.
