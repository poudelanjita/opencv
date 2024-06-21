import cv2
import numpy as np

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('frame2', result)
    print(frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()