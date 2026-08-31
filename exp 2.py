import cv2

# Read the image
image = cv2.imread("cv.jpg")

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# Display the blurred image
cv2.imshow("Blurred Image", blurred)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
