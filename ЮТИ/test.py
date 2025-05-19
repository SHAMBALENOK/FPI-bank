import cv2
import main

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    cv2.imshow('win', frame)

    if cv2.waitKey(1) == ord('q'):
        break
