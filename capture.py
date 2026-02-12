import cv2
import image
### i dont want to use if else statement to change operation. 
# I prefer to use composition where two or more class have methods with common name which i can call from another class
## in opencv we use seperate methods for reading an image and a video
## for these i created different classes to handle logic
## Capture mod class will have a instance of these classes based on input
class imageReader:
    def __init__(self, sourceName):
        self.source = sourceName
        self.frame =  cv2.imread(self.source)
    def getFrame(self):
        return self.frame is None,self.frame

class videoReader:
    def __init__(self, sourceName):
        self.source = sourceName
        self.frame =  cv2.VideoCapture(self.source)

    def getFrame(self):
        b,f = self.frame.read()
        return b,f

class CaptureMod:
    def __init__(self,reader):
        self.reader = reader
        self.image = image.imgProp(self.reader.getFrame()[1])
        self.mainMethod = self.reader.getFrame
    def main(self):
        b,self.image.img = self.mainMethod()

imReader = imageReader("1.jpg")
vReader = videoReader("video.mp4")
capt = CaptureMod(imReader)
while(1):
    capt.main()
    cv2.imshow("2",capt.image.img)

    cv2.waitKey(10) 