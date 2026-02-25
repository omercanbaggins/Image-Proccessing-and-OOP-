import cv2 
import time




class inputHandler:
    def __init__(self,img,namedWindow,captureMod):
        self.lastTime = time.time()
        self.current_time = time.time()
        self.isPressing = 0 
        self.mouseLast = (0,0)
        self.captureMod = captureMod
        self.mouseV = 0,0
        cv2.namedWindow(namedWindow)
        cv2.setMouseCallback(namedWindow,self.onMouse)
    def onMouse(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.isPressing = 1
            #print(x,y)
        if event == cv2.EVENT_LBUTTONUP:
            self.isPressing = 0
            self.captureMod.addNewPhysicalObject(x,y,self.mouseV,self.mouseV)
            #print(self.mouseV)
            cv2.circle(self.captureMod.image.img,(x,y),16,(41,123,24))

        if event == cv2.EVENT_MOUSEMOVE and self.isPressing==1:
            self.current_time = time.time()
            #print(self.current_time)
            x1,y1= self.mouseLast
        
            vx = x-x1
            vx = vx/(self.current_time-self.lastTime)
            vy = y-y1
            vy = vy/(self.current_time-self.lastTime)
            self.mouseV = (vx,vy)
            self.mouseLast = x,y
        self.lastTime = self.current_time

"""""""""""""""""""""""""""""""""""""""""""""""
objs = []

   
def drawObjects(img):
    for o in objs:
       cv2.circle(v,(o),16,(41,123,24))
v = None
VCapture = cv2.VideoCapture("video.mp4")

inputHandler(v,"mouseEvent")
while(1):
    _,v = VCapture.read()
    drawObjects(v)

    if(_):
        cv2.imshow("mouseEvent",v)
    cv2.waitKey(10)
"""""""""""""""""""""""""""""""""""""""""""""