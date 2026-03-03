import cv2
import numpy as np
cap =cv2.VideoCapture("example.mp4")

while(True):
     b,frame = cap.read()
     frame = cv2.resize(frame,(1280,720))
     frameGray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
     frameBlurred =cv2.GaussianBlur(frame,(1,1),1)
     _, binaryImage = cv2.threshold(frameBlurred,165,255,cv2.THRESH_BINARY)
     frameCanny = cv2.Canny(binaryImage,7,7)
     circles = cv2.HoughCircles(frameCanny,cv2.HOUGH_GRADIENT,1,20,
                        param1=50,param2=30,minRadius=5,maxRadius=55)
     blankImage = np.zeros_like(frame)
     if circles is not None:
        np.uint16(np.around(circles))
        for i in circles[0,:]:
            center = (int(i[0]),int(i[1]))
            radius = int(i[2])
            cv2.circle(blankImage,center,radius,(255,255,255),2)
     print(circles)
     cv2.imshow("normal",frameBlurred)

     cv2.imshow("cannyImage",binaryImage)
     cv2.imshow("blank",blankImage)

     cv2.waitKey(1)
     

