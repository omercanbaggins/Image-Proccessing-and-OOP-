import cv2

class imgProp:
    def __init__(self,img):
        ##if img.isinstance(cv2.UMat):
            self.width =img.shape[0]
            self.height=img.shape[1]
            self.img = img
            self.center = self.width//2,self.height//2
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
