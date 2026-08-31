import cv2
import numpy as np

# Read image
img = cv2.imread("cv.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel gradients
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Gradient magnitude
gradient = cv2.magnitude(grad_x, grad_y)
gradient = cv2.convertScaleAbs(gradient)

# Convert to BGR for addition
gradient = cv2.cvtColor(gradient, cv2.COLOR_GRAY2BGR)

# Sharpen image
sharpened = cv2.add(img, gradient)

cv2.imshow("Original", img)
cv2.imshow("Gradient Mask", gradient)
cv2.imshow("Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
