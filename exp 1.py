import cv2

# Read the image
image = cv2.imread("cv.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow("Grayscale Image", gray)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
