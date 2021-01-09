import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True :
    _,frame = cap.read()
    frame = cv2.flip(frame,1)

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower = np.array([45,200,20])
    upper = np.array([65,250,250])

    mask = cv2.inRange(hsv,lower,upper)

    cv2.imshow("window",frame)
    cv2.imshow("window1", hsv)
    cv2.imshow("window3", mask)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        break