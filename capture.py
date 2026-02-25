import callbacks
from callbacks import cv2
import image
import numpy as np
import time
import simpleMathOperations
### i dont want to use if else statement to change operation. 
# I prefer to use composition where two or more class have methods with common name which i can call from another class
## in opencv we use seperate methods for reading an image and a video
## for these i created different classes to handle logic
## Capture mod class will have a instance of these classes based on input
##there is a simple physics system where fundamental physisc properties are calculated except collision. 
##i had not enough time to complete the system so there is still problem with gravity and friction
## i have never worked on physics system that's why it is so primitive and buggy. I should watch computer graphics related videos and recall some of the physics topic 
## also there is a problem with x and y order which causes to wrong calculations to occur 
## in opencv top left starts with 0,0 which is inverse of cartesian coordinate system this may also cause incorrect vector operations

mouseLast = (0,0)

class imageReader:
    def __init__(self, sourceName):
        self.source = sourceName
        self.frame =  cv2.imread(self.source)
    def getFrame(self):
        return self.frame is None,self.frame

class PhysicalObject:
    def __init__(self,loc,mass,img):
        self.loc = (loc)
        self.totalForce = (0.0,0.0)
        self.Velocity = (0.0,0.0)
        self.mass = mass
        self.img = img
        if self.mass == 0 : self.mass = 0.001
    def changeAccelaration(self):
        acc = self.totalForce[0]/self.mass,self.totalForce[1]/self.mass
        self.Velocity= self.Velocity[0]+(acc[0]*0.01),self.Velocity[1]+(acc[1]*0.01)
        x,y = self.Velocity
        if abs(x) < 1e-3:
            x = 0.0
        if abs(y) < 1e-3:
            y = 0.0
        self.Velocity = (x, y)
    def addForce(self,f):
        self.totalForce = self.totalForce[0]+f[0],self.totalForce[1]+f[1]
        self.totalForce = (self.totalForce[0]),(self.totalForce[1])
    def changeLoc(self):
        self.loc = self.loc[0]+(self.Velocity[0]*0.01),self.loc[1]+(self.Velocity[1]*0.01)
    def getVelocityDirection(self):
        x,y = self.Velocity
     
        vLength = np.sqrt(np.square(x)+np.square(y))
        
        if (vLength> 1e-3):
            return (x/vLength,y/vLength)
        else:
            return 0,0
    def gravity(self):
        y,x = self.loc
        if (y>self.img.shape[0]):
            self.addForce((0,9.81*self.mass))
        else:
            self.totalForce = self.totalForce[0],0
            self.Velocity = self.Velocity[0],0
            return 

    def friction(self,fConstant):
        d1,d2 = self.getVelocityDirection()
        friction = (self.mass*fConstant*9.81*-1*d1,self.mass*fConstant*9.81*-1*d2)
        if(d1 == 0 and d2==0):
            #print(self.totalForce)
            return

        self.addForce(friction)

class videoReader:
    def __init__(self, sourceName):
        self.source = sourceName
        self.frame =  cv2.VideoCapture(self.source)

    def getFrame(self):
        b,f = self.frame.read()
        return b,f

class CaptureMod:
    def __init__(self,reader,windowName):
        self.reader = reader
        self.image = image.imgProp(self.reader.getFrame()[1])
        self.windowName = windowName
        self.mainMethod = self.reader.getFrame
        self.objList = []
        callbacks.inputHandler(self.image,windowName,self)

    def main(self):
        b,self.image.img = self.mainMethod()
        return b,self.image.img
    def addNewPhysicalObject(self,x,y,v,f):
        obj =  PhysicalObject((x,y),1,capt.image.img)
        self.addNewPhysicalObjWithRef(obj,v,f)
        

    def addNewPhysicalObjWithRef(self,obj,initV=(0,0),initF=0):
        self.objList.append(obj)
    
        obj.addForce(initV)
        cv2.circle(self.image.img,obj.loc,16,(123,51,23))
        #obj.addForce((155,-155))

    def checkObjectIsOutOfBorder(self,obj):
        world = self.image
        
        w,h = world.width,world.height
        x,y = obj.loc 
        print(x,y)
        if(x>w or x<0):
            print("collision is detected due to width")

            return True
        elif(y<0 or y>h):
            print("collision is detected")

            return True
        else:
            print("no border")
            return False


    def updateAllLocations(self):
        for i in self.objList:
            if(i.totalForce[0] !=0 and i.totalForce[1] !=0):
                #i.friction(0.03)
                pass
            else:
                pass
            #i.gravity()
            i.changeAccelaration()
            i.changeLoc()
            if(self.checkObjectIsOutOfBorder(i)):
                x,y = i.Velocity
                fx,fy = i.totalForce
                #i.addForce((-1*fx,-1*fy))
                i.Velocity = (-1*int(x),-1*int(y))
                i.addForce((-fx,-fy))
            if(i is not None and i.loc is not None):
                cv2.circle(self.image.img,(int(i.loc[0]),int(i.loc[1])),16,(123,51,23))
                #print(i.loc)

    

imReader = imageReader("1.jpg")
vReader = videoReader("video.mp4")
capt = CaptureMod(vReader,"mouseEvent")
math = simpleMathOperations.vectorMath()
A =simpleMathOperations.TwoDimensionalVector(100,200)
B = simpleMathOperations.vectorMath.rotateMatrice(A.MatriceAsColumn(),90)
B = simpleMathOperations.TwoDimensionalVector(B[0][0],B[0][1])
C = B.normalizeVector()
while(True):
    _,frame =  capt.main()
    v = frame
    A.drawVector(v,164,(400,400))
    B.drawVector(v,164,(400,400))
    C.drawVector(v,255,(470,470))
    """""""""""""""
    lines = cv2.HoughLinesP(processedImage,1,np.pi/180,20)
    for line in lines:
        if line is not None:
            x1,y1,x2,y2 = line[0]
            cv2.line(capt.image.img,(x1,y1),(x2,y2),(255,255,255))
    """""""""""""""
    capt.updateAllLocations()
    cv2.imshow("mouseEvent",capt.image.img)

    cv2.waitKey(10) 