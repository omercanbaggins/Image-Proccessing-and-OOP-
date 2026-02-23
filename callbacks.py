import cv2 
import time
mouseLast = (0,0)
cv2.namedWindow("mouseEvent")



class inputHandler:
    def __init__(self,img,namedWindow):
        self.lastTime = time.time()
        self.current_time = time.time()
        self.isPressing = 0 

        self.image = img
        cv2.setMouseCallback(namedWindow,self.onMouse)
    def onMouse(self,event,x,y,flags,param):
        if event == cv2.EVENT_LBUTTONDOWN:
            isPressing = 1
            cv2.circle(v,(x,y),16,(41,123,24))
            print(x,y)

            print("mouse was pressed")
        elif event == cv2.EVENT_LBUTTONUP:
            isPressing = 0
            cv2.circle(v,(x,y),16,(41,123,24))
            objs.append((x,y))
            v[y][x]=255
            print("mouse was released")

        elif event == cv2.EVENT_MOUSEMOVE and self.isPressing==1:
            current_time = time.time()
            print(current_time)
            x1,y1= mouseLast
            vx = x-x1
            vx = vx/(self.current_time-self.lastTime)
            vy = y-y1
            vy = vy/(self.current_time-self.lastTime)
            mouseLast = vx,vy
            print(mouseLast)
        self.lastTime = self.current_time

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