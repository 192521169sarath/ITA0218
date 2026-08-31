import cv2

# Open laptop built-in webcam
cap = cv2.VideoCapture(0)

while True:
    # Read video frame
    ret, frame = cap.read()

    if ret:
        # Display video
        cv2.imshow("Laptop Webcam", frame)

    # Press 'q' to close
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam
cap.release()

# Close all windows
cv2.destroyAllWindows()
