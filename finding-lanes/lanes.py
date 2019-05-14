import cv2
import numpy as np
import matplotlib.pyplot as plt


# imread() and imshow() functions will be used
# imread() - used to load image
# imshow() - renders the image

def canny(image):
    # This function converts an image to grayscale, reduces noise of gray image and uses canny algorithm to find edges

    # convert image to grayscale. cvtColor is used to convert image to different color scales
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    # reducing Noise
    '''
        arg1 - Image to smoothen
        arg2 - kernel grid to be used
        arg3 - deviation
     '''
    blur = cv2.GaussianBlur(gray, (5,5), 0)

    # Simple Edge Detection Canny(image, low_threshold, high_threshold), best low:high :: 1:3
    canny = cv2.Canny(blur, 50, 150)
    return canny

# read image from file and return as multidimensional numpy array containing relative intensities of each pixel in the image
image = cv2.imread('test_image.jpg')

# make a copy of image to work upon
lane_image = np.copy(image)

canny = canny(lane_image)

# after loading image, we have to render the image using imshow() function
cv2.imshow('result', canny)

# retain image for specified amount of time
cv2.waitKey(0)
