import cv2
import numpy as np

# Read image
img = cv2.imread("cv.jpg")

# Gaussian Blur
blur = cv2.GaussianBlur(img, (9,9), 10)

# Unsharp Masking
sharpened = cv2.addWeighted(img, 1.5, blur, -0.5, 0)

cv2.imshow("Original", img)
cv2.imshow("Unsharp Masking", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
