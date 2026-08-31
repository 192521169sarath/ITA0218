import cv2
import numpy as np

# Corresponding points
src = np.float32([[50,50],[300,50],[50,300],[300,300]])
dst = np.float32([[0,0],[400,0],[0,400],[400,400]])

# Homography using DLT algorithm
H, mask = cv2.findHomography(src, dst, method=0)

img = cv2.imread("cv.jpg")

result = cv2.warpPerspective(img, H, (400,400))

cv2.imshow("Original", img)
cv2.imshow("DLT Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
