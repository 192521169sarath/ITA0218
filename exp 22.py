import cv2
import numpy as np

# Read image
img = cv2.imread("cv.jpg")

# Laplacian mask with positive center coefficient
kernel = np.array([[0, -1, 0],
                   [-1, 4, -1],
                   [0, -1, 0]])

# Apply filter
laplacian = cv2.filter2D(img, -1, kernel)

# Sharpen image
sharpened = cv2.add(img, laplacian)

cv2.imshow("Original", img)
cv2.imshow("Sharpened (Positive Center)", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
