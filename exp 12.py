import cv2
import numpy as np

img = cv2.imread("cv.jpg")

# Four source points
pts1 = np.float32([[50,50],[300,50],[50,300],[300,300]])

# Destination points
pts2 = np.float32([[0,0],[400,0],[0,400],[400,400]])

# Perspective transformation matrix
matrix = cv2.getPerspectiveTransform(pts1, pts2)

# Apply transformation
result = cv2.warpPerspective(img, matrix, (400,400))

cv2.imshow("Original", img)
cv2.imshow("Perspective Transform", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
