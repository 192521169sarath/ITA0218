import cv2

# 1. Load the image
image = cv2.imread('cv.jpg')

# Check if image loads correctly
if image is None:
    print("Error: Could not read the image. Check the file path.")
    exit()

# --- METHOD 1: 90° / 180° Rotations (Clockwise & Counter-Clockwise) ---
# Rotate 90 degrees clockwise
rotate_90_cw = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Rotate 90 degrees counter-clockwise
rotate_90_ccw = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

# --- METHOD 2: Arbitrary Angle Rotations (Any angle) ---
# Using 45 degrees as an example
angle = 45 
height, width = image.shape[:2]
center = (width / 2, height / 2)

# Get the rotation matrix. (Note: Negative angle = clockwise, Positive = counter-clockwise)
matrix_cw = cv2.getRotationMatrix2D(center, -angle, 1.0)
matrix_ccw = cv2.getRotationMatrix2D(center, angle, 1.0)

# Apply the rotation
arbitrary_cw = cv2.warpAffine(image, matrix_cw, (width, height))
arbitrary_ccw = cv2.warpAffine(image, matrix_ccw, (width, height))

# --- DISPLAY OUTPUTS ---
cv2.imshow('Original Image', image)
cv2.imshow('Rotated 90 CW', rotate_90_cw)
cv2.imshow('Rotated 90 CCW', rotate_90_ccw)
cv2.imshow(f'Rotated {angle} deg CW', arbitrary_cw)
cv2.imshow(f'Rotated {angle} deg CCW', arbitrary_ccw)

# Wait for a key press and close all output windows
cv2.waitKey(0)
cv2.destroyAllWindows()
