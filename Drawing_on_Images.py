import cv2

img = cv2.imread('me.jpeg')

#cap = cv2.VideoCapture(0)

while True :
    #_,img = img.read()
    #img = cv2.flip(img,1)

    cv2.line(img,(330,460),(333,181),(0,0,255),2)
    cv2.rectangle(img,(334,182),(545,466),(255,255,255),3)
    cv2.circle(img,(430,350),(100),(0,0,255),thickness=3)
    cv2.putText(img,"Hey! how is it going!! ",(40,40), cv2.FONT_ITALIC,2,(0,2255,255),2)

    cv2.imshow("Window_Name", img)

    if cv2.waitKey(0) == 27:
        break

# cap.release()
# cv2.destroyAllWindows()


