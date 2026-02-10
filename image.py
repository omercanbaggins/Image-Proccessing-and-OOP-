import cv2
import numpy as np
class imgProp:
    def __init__(self,img):
        ##if img.isinstance(cv2.UMat):
            self.width =img.shape[0]
            self.height=img.shape[1]
            self.img = img
            self.center = self.width//2,self.height//2
            self.copyImg = img.copy()
    def getGrayScale(self):
        if self.img is not None:      ##we might often need grayscale of source image in order to apply various effect. I created spreate getter for it.
            return cv2.cvtColor(self.img,cv2.COLOR_RGB2GRAY)  
        else: return self.img
    def processImage(self):
        blurred = cv2.GaussianBlur(self.getGrayScale(),(5,15),5)
        _,threshImg = cv2.threshold(blurred,127,255,cv2.THRESH_BINARY)
        if(_):
            CannyImg = cv2.Canny(threshImg,50,150)
            return CannyImg
        
    def drawLinesAndCollide(self,LineLength,angleDiff=36,numberOfLine=10,collidingThreshold=100): ##draws lines and check if there is any colliding or not
        ##can be useful to detect specific features if i keep on improving
        a = 0
        for i in range(numberOfLine):
            for j in range(LineLength):
                y = self.center[0]+int(-j*np.sin(a*np.pi/180))
                x = self.center[1]+int(j*np.cos(a*np.pi/180))
                if(y<self.height and x<self.width):
                    if(self.getGrayScale()[y][x]>collidingThreshold):  ##threshold value

                        self.copyImg[y][x] = 0

            a = angleDiff*i
        
### i will add general menager for handling for showing multiple image and their various effects
## add more feauture for that class

class GeneralImageDisplay():
    def __init__(self):
        self.imageList = []
    def addToList(self,image):
        if(image.isinstance(cv2.Umat)):
            self.imageList.append()
    
    def showAllImages(self):
        index = 0
        for img in self.imageList:
            cv2.imshow("index",img)
            index+=1

print("hello")
