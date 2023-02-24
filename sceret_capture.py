import numpy as np
import cv2
import datetime
from PIL import ImageGrab
from win32api import GetSystemMetrics

# Video stuff.....

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

cv2.namedWindow("secret capture", cv2.WINDOW_NORMAL)
cv2.resizeWindow("secret cepture", 480, 270) #Here we are resizing the window to 480x270 so that the program doesn't run in full screen in the beginning

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.avi'
code = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(file_name, code, 16, (width, height))

# We will use a loop
while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height)) #capturing screenshot
    img_np = np.array(img) #converting the image into numpy array representationz
    final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB) #converting the BGR image into RGB image
    cv2.imshow('secret capture',final)#display screen/frame being recorded
    out.write(final)#writing the RBG image to file
    if cv2.waitKey(1) == ord('q'): #Wait for the user to press 'q' key to stop the recording
        break


