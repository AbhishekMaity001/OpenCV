import cv2
import numpy as np

img = cv2.imread('me.jpeg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img2 = cv2.blur(img,(5,5))

#_,img = cv2.threshold(img,50,58,cv2.THRESH_BINARY)
# img2.erode(img,np.ones((5,5)),iterations=3)

img = img[180:450,330:550] # [ yvalue : yvalue , xvalue : xvalue]
while True:
    cv2.imshow('window',img)
    cv2.imshow('window1',img2)

    if cv2.waitKey(0)==27:
        cv2.destroyAllWindows()
        break