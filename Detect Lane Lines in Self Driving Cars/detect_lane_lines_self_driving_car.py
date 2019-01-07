----------------------------------------------------------------------------
### PROJECT: PART I - SELECT(MASK) WHITE PIXELS OUT OF THE COLORED IMAGE ###
----------------------------------------------------------------------------
#importing all the necessary libraries
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

#read the image and display it
image_color = mpimg.imread('image_lane_c.jpg')
image_color.shape
plt.imshow(image_color)

#creting a copy of an image
image_copy = np.copy(image_color)
image_copy.shape

#any value that is not white colour,(everything below 200) set to zero
image_copy[ (image_copy[:,:,0] < 200) | (image_copy[:,:,1] < 200) | (image_copy[:,:,2] < 200) ] = 0

#display the image                 
plt.imshow(image_copy, cmap = 'gray')
plt.show()

--------------------------------------------------------------------------------
### PROJECT: PART II - SELECT(MASK) WHITE PIXELS OUT OF THE GRAY SCALE IMAGE ###
--------------------------------------------------------------------------------
#importing all the necessary libraries
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

#read the image and display it
image_color = mpimg.imread('image_lane_c.jpg')
image_color.shape
plt.imshow(image_color)

#convert the image into grayscale image
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap = 'gray')
image_gray.shape

#creting a copy of an image
image_copy = np.copy(image_gray)
image_copy.shape

#any value that is not white colour,(everything below 250) set to zero
image_copy[ (image_copy[:,:] < 250) ] = 0

#display the image                 
plt.imshow(image_copy, cmap = 'gray')
plt.show()

--------------------------------------------------------------
### PROJECT: PART III - REGION OF INTEREST (ROI) SELECTION ###
--------------------------------------------------------------
#importing all the necessary libraries
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

#read the image and display it
image_color = cv2.imread('image_lane_c.jpg')
# import image as RGB instead of BGR
# image_color = mpimg.imread('image_lane_c.jpg')
cv2.imshow('Original Image', image_color)
cv2.waitKey()
cv2.destroyAllWindows()

#settip up the height and width
height, width = image_color.shape[:2]
height
width
plt.imshow(image_color)
image_color.shape

#convert the image into grayscale image
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap = 'gray')
image_gray.shape

#select region of interest (ROI)
#(0,0) - upper left; width,height) - bottom right
ROI = np.array([[(100, height),(410, 350), (530, 350), (800, height)]], dtype=np.int32)    

#define a blank image with all zeros (ie: black) 
blank = np.zeros_like(image_gray)   
blank.shape

#fill the Region of interest with white color (ie: 255)!
mask = cv2.fillPoly(blank, ROI, 255)
    
#perform bitwise AND operation to select only the region of interest
masked_image = cv2.bitwise_and(image_gray, mask)
masked_image.shape
plt.imshow(masked_image, cmap = 'gray')










