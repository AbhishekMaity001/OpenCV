# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2


''' img = cv2.imread('C:/Users/Abhishek Maity/Pictures/Camera Roll/proffile (2).jpg')
while True :
    cv2.imshow("window",img)

    if(cv2.waitKey(0)) == ord('q'):
        break

#cv2.imwrite("me.jpeg",img)
cv2.destroyAllWindows()  '''

cap = cv2.VideoCapture(0)

while True:

    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.imshow("window",frame)

    if cv2.waitKey(1) == 27:
        break

cap.release() # just relese the resource (webcam)
cv2.destroyAllWindows()
# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
