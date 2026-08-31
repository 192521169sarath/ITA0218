import cv2

# Read the main image
img = cv2.imread("cv.jpg")

# Read the image to be pasted
small_img = cv2.imread("sam.jpg")

# Check whether images are loaded
if img is None or small_img is None:
    print("Error: Image not found")
    exit()

# -------------------------------
# CROPPING
# -------------------------------

# Crop a portion of the main image
# Format: image[y1:y2, x1:x2]
crop = img[100:300, 100:300]

# Save cropped image
cv2.imwrite("cropped.jpg", crop)

# -------------------------------
# COPYING AND PASTING
# -------------------------------

# Resize the small image
small_img = cv2.resize(small_img, (200, 150))

# Position where the image will be pasted
x = 300
y = 100

# Copy the image
img_copy = img.copy()

# Paste the small image inside the main image
img_copy[y:y+150, x:x+200] = small_img

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Cropped Image", crop)
cv2.imshow("Image After Copy and Paste", img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
