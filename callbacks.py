import cv2 
import time
mouseLast = (0,0)
cv2.namedWindow("mouseEvent")

lastTime = time.time()
current_time = time.time()
v = None
isPressing = 0 
def onMouse(event,x,y,flags,param):
    global isPressing,mouseLast,lastTime,current_time
    if event == cv2.EVENT_LBUTTONDOWN:
        isPressing = 1
        cv2.circle(v,(x,y),16,(41,123,24))
        print(x,y)

        print("mouse was pressed")
    elif event == cv2.EVENT_LBUTTONUP:
        isPressing = 0
        cv2.circle(v,(x,y),16,(41,123,24))
        v[y][x]=255
        print("mouse was released")

    elif event == cv2.EVENT_MOUSEMOVE and isPressing==1:
        current_time = time.time()
        print(current_time)
        x1,y1= mouseLast
        vx = x-x1c
        vx = vx/(current_time-lastTime)
        vy = y-y1
        vy = vy/(current_time-lastTime)
        mouseLast = vx,vy
        print(mouseLast)
    lastTime = current_time
   


cv2.setMouseCallback("mouseEvent",onMouse)
VCapture = cv2.VideoCapture("video.mp4")
while(1):
    _,v = VCapture.read()
    if(_):
        cv2.imshow("mouseEvent",v)
    cv2.waitKey(10) 