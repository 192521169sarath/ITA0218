import cv2
import numpy as np

# Read image
img = cv2.imread("cv.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel X
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Convert to absolute values
sobelx = cv2.convertScaleAbs(sobelx)

cv2.imshow("Original", img)
cv2.imshow("Sobel X", sobelx)

cv2.waitKey(0)
cv2.destroyAllWindows()
