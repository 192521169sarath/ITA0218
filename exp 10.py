import cv2
import numpy as np

# Load image
img = cv2.imread('cv.jpg')
if img is None:
    print("Error: Could not read image.")
    exit()

rows, cols = img.shape[:2]

# Define translation: shift 100 pixels right, 50 pixels down
tx, ty = 100, 50
translation_matrix = np.float32([[1, 0, tx], 
                                 [0, 1, ty]])

# Apply translation
moved_img = cv2.warpAffine(img, translation_matrix, (cols, rows))

# Display result
cv2.imshow('Original Image', img)
cv2.imshow('10. Moved Image', moved_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
