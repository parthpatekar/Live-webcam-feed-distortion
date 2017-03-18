import numpy as np
import cv2
import math
"""
# -*- coding: utf-8 -*-

Created on Tue Mar 14 00:15:29 2017

@author: Parth Patekar

"""
#setting a constant
k=0.0000000000001

#Start capturing from webcam  
cap = cv2.VideoCapture(0)

#Set width of the captured video
cap.set(3,320)

#Set height of the captured video
cap.set(4,240)

#Start a window named 'Frame'
cv2.namedWindow("Frame")

#For each frame
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
#<--------------------------------Our operations on each frame come here---------------------------->

    #Get the shape of the frame
    (h,w,ch) = frame.shape
    
    #Getting the location of the centre of the frame
    (cX,cY)=(math.ceil(w/2),math.ceil(h/2))
    
    #Running a single loop to parse over the 2-D matrix of the image.
	#In this all the operations are applied to all three channels.
    for j in range(h*w):        
        #Making a copy of the loop counter, so that the loop runs uninterrupted
        i=j
        
        #Change the coordinates to the center of the grid figure
        xd=(i/h)-cX  
        yd=(i%h)-cY

        #Just for calibration
        if xd==0 and yd==0:  
            (xu,yu)=((i/h),(i%h))
            frame[yu,xu]=frame[(i%h),(i/h)]
            i+=1
            continue
        
        ##Converting the cartesian coordinates (x, y) to polar (r, theta)
        #find values of distorted radius by following equation
        rd=math.sqrt(xd*xd+yd*yd)
        rd_2=rd*rd
        
        #find the value of undistorted radius by following equation
        ru=rd/(1 + k*rd_2*(1 + rd_2 + rd_2*rd_2))
        
        #convert the new radius to cartesian coordinates
        xuf=math.ceil(ru*xd/rd)+cX
        yuf=math.ceil(ru*yd/rd)+cY

        #Check whether the new coordinates are going out of the frame or not, if so then skip them and continue
        if xuf > w-1 or yuf > h-1:
            i+=1
            continue
        
        #writing in the frame
        frame[(i%h),(i/h)]=frame[int(yuf),int(xuf)] 

    #The output window will be as set - 320p x 240p, so we resize it to get a bigger window
    frame_display = cv2.resize(frame, (w*2, h*2), interpolation=cv2.INTER_CUBIC)
    
    #Display the resulting frame
    cv2.imshow('distorted',frame_display)   
    
    #Quit on Esc key
    if cv2.waitKey(1) == 27:
        break
  
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()