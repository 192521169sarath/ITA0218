import cv2
import numpy as np

img = cv2.imread("cv.jpg", cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Error: Image not found")
    exit()

# Sobel X kernel
kernel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

# Sobel Y kernel
kernel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

# Convolution
edge_x = cv2.filter2D(img, cv2.CV_64F, kernel_x)
edge_y = cv2.filter2D(img, cv2.CV_64F, kernel_y)

# Convert to absolute values
edge_x = cv2.convertScaleAbs(edge_x)
edge_y = cv2.convertScaleAbs(edge_y)

# Combine X and Y boundaries
boundary = cv2.addWeighted(edge_x, 0.5, edge_y, 0.5, 0)

cv2.imshow("Original Image", img)
cv2.imshow("Boundary using Convolution", boundary)

cv2.waitKey(0)
cv2.destroyAllWindows()
