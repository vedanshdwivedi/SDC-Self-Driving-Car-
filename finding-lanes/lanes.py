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


def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10) # arg4 is BGR color (blue) #arg5 is line thickness
    return line_image

def region_of_interest(image):
    # identify the region of interest in the image
    height = image.shape[0]

    # the below coords have been figured out using matplotlib library
    polygons = np.array([
    [(200, height), (1100, height), (550, 250)]
    ])

    # creating a black background
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image




# read image from file and return as multidimensional numpy array containing relative intensities of each pixel in the image
image = cv2.imread('test_image.jpg')

# make a copy of image to work upon
lane_image = np.copy(image)

canny = canny(lane_image)

cropped_image = region_of_interest(canny)

# to identify edges using Hough Transform (refer README), p = x cosƟ + y sinƟ
# arg1 - Image
# arg2 - Specify resolution of hough accumulator array (p)
# arg3 - Specify resolution of hough accumulator array (Ɵ)
# arg4 - threshold (minimum no. of votes needed to accept a candidate line)
# arg5 - placeholder array
# arg6 - length of line that we will accept as output (in pixels)
# arg7 - Maximum Gap between lines acceptable
# OPTIMIZE: use hit and trial method to find arg4
# arg2 and arg3 define the size of bins, larger the bins, less is the precision
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)

line_image = display_lines(lane_image, lines)

# Multiply lane_image with 0.8 to make it darker, line_image has 20% more weight so it will be more visible
# arg5 is gamma component
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)

# after loading image, we have to render the image using imshow() function
cv2.imshow('result', combo_image)

# retain image for specified amount of time
cv2.waitKey(0)
