import math
import numpy as np

class vectorMath:
    pi = np.pi
    def convertToDegree(radianValue):
        degree = radianValue* vectorMath.pi/180
        return degree
    def calcLength(vector):
        x,y = vector
        length = np.sqrt(np.pow(x,2)+np.pow(y,2))
        return  length
    def normalize(v1):
        x,y = v1.x,v1.y
        vLength = v1.getLength()
        print(vLength)
        return TwoDimensionalVector(x/vLength,y/vLength)
    def dotProduct(self,pt1,pt2):
        x,y = pt1
        x2,y2 =pt2
        multOfLengths = self.calcLength(pt1)*self.calcLength(pt2)
        cos = ((x*x2)+(y*y2))/multOfLengths
        degree= np.acos(cos)*180/np.pi
        return degree
    def vectorAddition(self,v1,v2):
        x1,y1 = v1
        x2,y2 = v2
        v3 = (x1+x2),(y1+y2) 
        return v3,TwoDimensionalVector(v3)
    
class TwoDimensionalVector:
    def __init__(self,x=1,y=1):
        self.x =x
        self.y =y 
    def getLength(self):
        return vectorMath.calcLength((self.x,self.y))
    def normalizeVector(self):
        return vectorMath.normalize((self))
    def opposite(self):
        return TwoDimensionalVector(-1*self.x,-1*self.y)

v1 = TwoDimensionalVector(7,5)
norm = v1.normalizeVector()
print(norm.x,norm.y)