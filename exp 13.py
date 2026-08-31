import cv2
import numpy as np

cap = cv2.VideoCapture("sample.mp4")

pts1 = np.float32([[100,100],[500,100],[100,400],[500,400]])
pts2 = np.float32([[0,0],[400,0],[0,400],[400,400]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    transformed = cv2.warpPerspective(frame, matrix, (400,400))

    cv2.imshow("Original", frame)
    cv2.imshow("Perspective Video", transformed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
