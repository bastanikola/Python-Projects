-----------------------------------------------------------
### PROJECT: PART I - CONVERT COLOR IMAGES TO GRAYSCALE ###
-----------------------------------------------------------
#importing all the necessary libraries
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

image = input("Enter a path to your picture: ")
image_color = mpimg.imread(image)

image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
plt.imshow(image_gray, cmap = 'gray')

#save the image in greyscale
new_gray = input("Enter a path and new name for the gray picture: ")
cv2.imwrite(new_gray, image_gray)

----------------------------------------------------------
### PROJECT: PART II - CONVERT COLOR IMAGES TO CARTOON ###
----------------------------------------------------------
'''Cartoon Effect
Stylization aims to produce digital imagery with a wide variety of effects
not focused on photorealism. Stylization can abstract regions of low contrast
while preserving, or enhancing, high-contrast features.

Parameters:
src Input 8-bit 3-channel image.
dst Output image with the same size and type as src.
sigma_s Range between 0 to 200.
sigma_r Range between 0 to 1.

NOTE:
sigma_s - controls how much the image is smoothed - the larger its value, the more
smoothed the image gets, but it's also slower to compute.
sigma_r - is important if you want to preserve edges while smoothing the image.
Small sigma_r results in only very similar colors to be averaged (i.e. smoothed),
while colors that differ much will stay intact.'''

#importing all the necessary libraries
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2

image = input("Enter a path to your picture: ")
color_image = cv2.imread(image)

#cartoon effect
cartoon_image = cv2.stylization(color_image, sigma_s=200, sigma_r=0.3)

#pencil sketch effect
cartoon_image, cartoon_image2  = cv2.pencilSketch(color_image, sigma_s=60, sigma_r=0.1)

cv2.imshow('cartoon', cartoon_image)
cv2.waitKey()
cv2.destroyAllWindows() 
