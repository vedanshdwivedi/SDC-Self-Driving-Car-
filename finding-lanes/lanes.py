import cv2

# imread() and imshow() functions will be used
# imread() - used to load image


# read image from file and return as multidimensional numpy array containing relative intensities of each pixel in the image
image = cv2.imread('test_image.jpg')

# after loading image, we have to render the image using imshow() function
cv2.imshow('result', image)

# retain image for specified amount of time
cv2.waitKey(0)
