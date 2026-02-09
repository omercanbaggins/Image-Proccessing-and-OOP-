from image import imgProp 
import cv2
import numpy as np
print("hello face Detection")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
def findVectorLenght(vect1):
    x,y = vect1
    length = np.sqrt(np.pow(x,2)+np.pow(y,2))
    return  length
def findAngle(pt1,pt2):
    x,y = pt1
    x2,y2 =pt2
    multOfLengths = findVectorLenght(pt1)*findVectorLenght(pt2)
    cos = ((x*x2)+(y*y2))/multOfLengths
    degree= np.acos(cos)*180/np.pi
    return degree

b = 1
img = cv2.imread("1.jpg")
img = cv2.resize(img,(640,480))
imgC = imgProp(img)
imgC.processImage()
while(b == 1):
    gray = imgC.getGrayScale()
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    if len(faces)>0:

        for i in faces:
            x,y,width,height = i
            cv2.rectangle(imgC.img,(x,y),(x+width,y+height),(255,255,255),16)
            centerRect = (x+width//2),(y+height//2)
            imgCenter = imgC.center
            print(findAngle(imgCenter,centerRect))

            cv2.line(imgC.img,imgCenter,centerRect,(50,50,50),12)
        cv2.imshow("normalImage",imgC.img)
    cv2.imshow("",img)
    b = cv2.waitKey(0)
cv2.destroyAllWindows()
    