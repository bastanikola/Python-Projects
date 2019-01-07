----------------------------------------
### PROJECT - FACE AND EYE DETECTION ###
----------------------------------------
-------------------------------
### STEP 1: DETECT ONE FACE ###
-------------------------------
import numpy as np
import cv2

image_c = cv2.imread('Trudeau.jpg')
image_g = cv2.cvtColor(image_c, cv2.COLOR_BGR2GRAY)

cv2.imshow('Trudeau in Color', image_c)
cv2.waitKey()
cv2.destroyAllWindows() 

cv2.imshow('Trudeau in Grayscale', image_g)
cv2.waitKey()
cv2.destroyAllWindows() 

#get CascadeClassifier (trained model) 
face_detection = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
'''
CascadeClassifier.detectMultiScale(input image, Scale Factor , Min Neighbors)

    SCALE FACTOR

    - Specifies how much reduction takes place in the image size each time during pyramiding process.
    - For 1.2, it means image is reduced by 20% each time it’s scaled.
    - Min Neighbors

    - Parameter specifying how many neighbors each candidate rectangle should have to retain it.
    - Set it to a number between 3 and 6.
    - This parameter will affect the quality of the detected faces.
    - Higher value results in less detections but with higher quality.
'''

#the face classifier returns the region of interest in a tuple 
#two points: upper left and bottom right coordinates
faces = face_detection.detectMultiScale(image_c, 1.1, 5)
faces.shape
faces
faces[:,1]

x = faces[:, 0]
y = faces[:, 1]
w = faces[:, 2]
h = faces[:, 3]

cv2.rectangle(image_c, (x,y), (x+w,y+h), (0,255,255), 3)
cv2.imshow('Single Face Detection', image_c)
cv2.waitKey(0)
    
cv2.destroyAllWindows()

---------------------------------
### STEP 2: DETECT MUTLIPLE FACES
---------------------------------
image_c = cv2.imread('Scientists.jpg')
image_g = cv2.cvtColor(image_c, cv2.COLOR_BGR2GRAY)

cv2.imshow('Scientists in Color', image_c)
cv2.waitKey()
cv2.destroyAllWindows() 

cv2.imshow('Scientists in GrayScale', image_g)
cv2.waitKey()
cv2.destroyAllWindows() 

#get CascadeClassifier (trained model)
face_detection = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
faces = face_detection.detectMultiScale(image_c, 1.08, 7)
for (x,y,w,h) in faces:
    cv2.rectangle(image_c, (x,y), (x+w,y+h), (0,255,255), 3)
    #cv2.imshow('Single Face Detection', image_c)
    #cv2.waitKey(0)
    
cv2.imshow('Single Face Detection', image_c)
cv2.waitKey(0)    
cv2.destroyAllWindows()

-------------------------------------
### STEP 3: DETECT EYES AND FACES ###
-------------------------------------
image_c = cv2.imread('Trudeau.jpg')

face_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_frontalface_default.xml')
eye_classifier = cv2.CascadeClassifier('Haarcascades/haarcascade_eye.xml')

faces = face_classifier.detectMultiScale(image_c, 1.2, 5)

for (x,y,w,h) in faces:
    cv2.rectangle(image_c,(x,y),(x+w,y+h),(0,255,255), 3)
    cv2.imshow('Trudeau Face and Eyes',image_c)
    cv2.waitKey(0)
    
    #select the face
    face_region = image_c[y:y+h, x:x+w]
    
    eyes = eye_classifier.detectMultiScale(face_region)
    
    for (eyes_x, eyes_y, eyes_w,eyes_h) in eyes:
        cv2.rectangle(face_region,(eyes_x, eyes_y),(eyes_x + eyes_w, eyes_y + eyes_h), (0,255,0),3)
        cv2.imshow('Trudeau Face and Eyes',image_c)
        cv2.waitKey(0)
    
cv2.destroyAllWindows()

cv2.imshow('Face Region',image_c[y:y+h, x:x+w])
cv2.waitKey(0)
cv2.destroyAllWindows()   
