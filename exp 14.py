import cv2
import numpy as np

img = cv2.imread("cv.jpg")

src = np.float32([[56,65],[368,52],[28,387],[389,390]])
dst = np.float32([[0,0],[400,0],[0,400],[400,400]])

# Compute Homography
H, status = cv2.findHomography(src, dst)

# Warp image
output = cv2.warpPerspective(img, H, (400,400))

cv2.imshow("Original", img)
cv2.imshow("Homography", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
