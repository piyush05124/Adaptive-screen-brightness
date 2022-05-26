import cv2
from auto_screen_brightness import *
import keyboard as kb
import cv2
import time
import numpy as np
import screen_brightness_control as sbc
import os
import sys
# Create a VideoCapture object and read from input file
cap = cv2.VideoCapture(0)
   
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video  file")
   
# Read until video is completed
font = cv2.FONT_HERSHEY_SIMPLEX
  
# org
org = (50, 50)
  
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (255, 0, 0)
  
# Line thickness of 2 px
thickness = 2
while(cap.isOpened()):
      
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:
   
    # Display the resulting frame
    #img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    bg=avg_brightness(frame)
    sbc.set_brightness(round(bg-2))
    cv2.putText(frame, str(bg), org, font, 
                   fontScale, color, thickness, cv2.LINE_AA)
    #cv2.imshow('Frame', frame)
    
    if kb.is_pressed('space'):
        print('pressed')
        exit()
        time.sleep(0.1)
        #kb.write('exit()')
        kb.press_and_release('enter')
##        

    # Press Q on keyboard to  exit
    #if cv2.waitKey(25) & 0xFF == ord(' '):
        #break
   
  # Break the loop
  else: 
    break
   
# When everything done, release 
# the video capture object
cap.release()
   
# Closes all the frames
cv2.destroyAllWindows()

