import cv2 
import numpy as np
import math
import simpleMathOperations as MM
fov = 1
loc = 0,0
x1 = 0
def onMouse(event, x, y, flags, param):
    global fov, loc, x1
    
    if event == cv2.EVENT_MOUSEWHEEL:

        if flags > 0:
            fov += 0.1
        else:
            fov -= 0.1
        if fov <= 0.1:
            fov = 0.1
    if event == cv2.EVENT_RBUTTONDOWN:
        x1+=1
    if event == cv2.EVENT_LBUTTONDOWN:
        x1-=1
    loc = x,loc[1]
vertices = np.array([(1,5,9),(1,10,9),(3,5,9),(3,10,9),[1,5,18],(1,10,18),(3,5,18),(3,10,18)])

cv2.namedWindow("world")
cv2.setMouseCallback("world",onMouse)
TwoDVertices = []
world = np.zeros((640,480))
while(True):
    world = np.zeros((480, 640, 3), dtype=np.uint8)
    TwoDVertices = []
    key = cv2.waitKey(10) & 0xFF 
    for i in vertices:
        print(i)
        x,y = i[0]/i[2]*fov , i[1]/i[2]*fov
        x=x*200+loc[0]
        y = y*200+ loc[1]
        x =int(x)
        y = int(y)
        try:
            world[y][x]=255
        except IndexError:
            pass

        TwoDVertices.append((x,y))
    previous = TwoDVertices[0]
    for j in TwoDVertices:
        for i in TwoDVertices:
            if(previous == i):
                pass
            cv2.line(world,j,i,(255,255,255),1)

    cv2.imshow("world",world) 

    if key == ord('q'):  
        cv2.destroyAllWindows()

        break
