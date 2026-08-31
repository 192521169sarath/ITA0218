import cv2
import numpy as np

# Read image
img = cv2.imread("cv.jpg")

# Blur image
blur = cv2.GaussianBlur(img, (9,9), 10)

# High-Boost factor
A = 2.0

# High-Boost Sharpening
highboost = cv2.addWeighted(img, A, blur, -(A-1), 0)

cv2.imshow("Original", img)
cv2.imshow("High Boost", highboost)

cv2.waitKey(0)
cv2.destroyAllWindows()
