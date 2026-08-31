import cv2
import numpy as np

# Read the image
image = cv2.imread("cv.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 100, 200)

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Dilate the edges
dilated = cv2.dilate(edges, kernel, iterations=1)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Edges", edges)
cv2.imshow("Dilated Image", dilated)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
