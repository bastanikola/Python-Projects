-------------------------------------------------
### PROJECT: SKETCH EFFECTS USING LIVE WEBCAM ###
-------------------------------------------------
#importing all necessary libraries
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

'''we are taking image here because, in a nutshell,
video is nothing more than a series of images. We
will call this function in a while loop
sigma_s = from 0 to 200
sigma_r = from 0 to 1'''

#using cartoon stylization technique
def Cartoon(image_color):
    output_image = cv2.stylization(image_color, sigma_s=100, sigma_r=0.3)
    return output_image

#using canny edge detection technique on a gray scale image
def LiveCamEdgeDetection_canny(image_color):    
    #defining spec of the edges
    threshold_1 = 30
    threshold_2 = 80
    
    #transfering image into gray scale
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)

    #running canny
    canny = cv2.Canny(image_gray, threshold_1, threshold_2)
    return canny 

#main function; initializing webcam and apply edge detection
cap = cv2.VideoCapture(0)

while True:
    #cap.read is used for capturing our webcam
    #cap.read returns a ret: bool to indicate success(1) or fail(0).
    #cap.read returns a frame: actual image
    ret, frame = cap.read()

    #here we are using cartoon frame
    cv2.imshow('Live Edge Detection', Cartoon(frame))

    #here we are using canny edge frame
    #in order to use it, uncomment the code and comment the cartoon one
    #cv2.imshow('Live Edge Detection', LiveCamEdgeDetection_canny(frame))
    cv2.imshow('Webcam Video', frame)
    #13 is Enter Key
    if cv2.waitKey(1) == 13:
        break
    
#camera release   
cap.release()
cv2.destroyAllWindows()    
