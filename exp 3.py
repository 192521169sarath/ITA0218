import cv2

# Read the image
image = cv2.imread("cv.jpg")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur (reduces noise)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using Canny
edges = cv2.Canny(blurred, 100, 200)

# Display the result
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Detection", edges)

# Wait for a key press and close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
