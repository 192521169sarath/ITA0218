import cv2
import numpy as np

# Load image
img = cv2.imread('cv.jpg')
if img is None:
    print("Error: Could not read image.")
    exit()

rows, cols = img.shape[:2]

# Map 3 points: Top-Left, Top-Right, Bottom-Left
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

# Calculate transformation matrix and apply
affine_matrix = cv2.getAffineTransform(pts1, pts2)
affine_img = cv2.warpAffine(img, affine_matrix, (cols, rows))

# Display result
cv2.imshow('Original Image', img)
cv2.imshow('11. Affine Transformation', affine_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
