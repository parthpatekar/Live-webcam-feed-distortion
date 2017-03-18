It is a program which applies distortion effect to the live webcam feed.
In this program, we use opencv to apply distortion effect to a live webcam feed.   
For this we start recording, extract each recording frame-by-frame and process it. 
The frame obtained is a 3-D matrix where each dimension represents height, width and channels (RGB) respetively.						     
Now we run a for loop to get coordinates of pixels.				     
The centre of the frame is at the top-left corner, so we bring it to the centre of the frame.									     
We have the coordinates of the pixels in cartesian form, now we convert them to polar coordinates.								     
The radius obtained is now transformed using a equation.			     
Skip and continue the where the new coordinates go out of the frame.		     
Display the output frame.							     
Resize the window.
Python OpenCV is used to do this
