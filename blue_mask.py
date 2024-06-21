import cv2
import numpy as np

capture = cv2.VideoCapture(0)
while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))
    
    img = cv2.line(frame, (0, 0), (width, height), (255,0, 255), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 20)
    img = cv2.circle(img, (300, 300), 60,(0, 0,255), 5 )
    
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(img, 'Denied', (height, 200-10), font, 2, (0,0,255), 3, cv2.LINE_AA)

    cv2.imshow('frame', img)
    print(frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()