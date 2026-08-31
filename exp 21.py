import cv2
import numpy as np

# Read image
img = cv2.imread("cv.jpg")

# Laplacian mask with diagonal extension
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

# Apply filter
laplacian = cv2.filter2D(img, -1, kernel)

# Sharpen image
sharpened = cv2.subtract(img, laplacian)

cv2.imshow("Original", img)
cv2.imshow("Sharpened (Diagonal Extension)", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
