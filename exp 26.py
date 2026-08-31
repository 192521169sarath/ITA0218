import cv2

# Read image
img = cv2.imread("cv.jpg")

# Watermark text
text = "Copyright 2026"

# Add watermark
cv2.putText(img,
            text,
            (50, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (255, 255, 255),
            2,
            cv2.LINE_AA)

cv2.imshow("Watermarked Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
