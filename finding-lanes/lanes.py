import cv2
import numpy as np

# imread() and imshow() functions will be used
# imread() - used to load image


# read image from file and return as multidimensional numpy array containing relative intensities of each pixel in the image
image = cv2.imread('test_image.jpg')

# make a copy of image to work upon
lane_image = np.copy(image)

# convert image to grayscale. cvtColor is used to convert image to different color scales
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)

# after loading image, we have to render the image using imshow() function
cv2.imshow('result', gray)

# retain image for specified amount of time
cv2.waitKey(0)
