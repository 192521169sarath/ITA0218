import cv2

# Load your source image
image = cv2.imread('cv.jpg')

# Scale UP (Make it 2x bigger)
# INTER_CUBIC offers high quality for upscaling
bigger = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC)

# Scale DOWN (Make it 2x smaller)
# INTER_AREA prevents pixel aliasing/distortion during downscaling
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Save the generated outputs
cv2.imwrite('bigger_image.jpg', bigger)
cv2.imwrite('smaller_image.jpg', smaller)
