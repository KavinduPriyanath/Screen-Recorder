# Screen-Recorder
A simple Screen Recorder made using Numpy, OpenCV and Pyautogui Python libraries.<br/><br/>
How it happens?

First create a VideoWriter Object using opencv.
Necessary parameters in VideoWriter Object,<br/>
&nbsp;	1) Output filename<br/>
	2) Resolution<br/>
		-Here the correct Screen Size is needed or writing to file won't work. Can use pyautogui.size() to get the size of the primary monitor<br/>
	3) FPS<br/>
	4) Video Codec (XVID, MJPG, X264)<br/>



Inside the infinite loop,<br/>
	1) Capture a screenshot using pyautogui<br/>
	2) Convert that screenshot to a numpy array<br/>
	3) Write it to the output file using the VideoWriter Object<br/>

cvtColor() is used for Colour Space Conversion (To RGB) because OpenCV use BGR by default.<br/>

img = pyautogui.screenshot(region=(0,0,200,200)) can also be used to capture only a part of the screen but the would need to change the screen resolution too. Parameters are (top, left, width, height).<br/>In this case, <br/>
	resolution = (200,200)<br/>

Finally we close the VideoWriter using ouput.release() and then destroy all opened windows.
