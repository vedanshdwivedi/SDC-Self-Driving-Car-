import cv2
import numpy as np
import matplotlib.pyplot as plt


def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1-intercept)/slope)
    x2 = int((y2-intercept)/slope)
    return np.array([x1, y1, x2, y2])

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
        for x1, y1, x2, y2 in lines:
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


def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_fit_average = np.average(left_fit, axis=0)
    right_fit_average = np.average(right_fit, axis=0)
    left_line = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    return np.array([left_line, right_line])


# read image from file and return as multidimensional numpy array containing relative intensities of each pixel in the image
image = cv2.imread('test_image.jpg')

# make a copy of image to work upon
lane_image = np.copy(image)

'''

canny_image = canny(lane_image)

cropped_image = region_of_interest(canny_image)

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
averaged_lines = average_slope_intercept(lane_image, lines)
line_image = display_lines(lane_image, averaged_lines)

# Multiply lane_image with 0.8 to make it darker, line_image has 20% more weight so it will be more visible
# arg5 is gamma component
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)

# after loading image, we have to render the image using imshow() function
cv2.imshow('result', combo_image)

# retain image for specified amount of time
cv2.waitKey(0)

'''



cap = cv2.VideoCapture("test2.mp4")
while(cap.isOpened()):
    _, frame = cap.read()
    canny_image = canny(frame)
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
    averaged_lines = average_slope_intercept(frame, lines)
    line_image = display_lines(frame, averaged_lines)
    combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
    cv2.imshow('result', combo_image)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
