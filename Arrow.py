from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Utility import *
from math import pi, tan

def getArrowPath(p1,p2,pathWidth=1,d1=1,d2=1,theta=pi/2,r1=0,r2=0):
    path = QPainterPath(p1)
    dist = norm(p1 - p2)
    if dist == 0:  return path
    if dist < d1 + d2:
        k = dist/(d1 + d2)
        d1,d2 = k*d1,k*d2
        pathWidth *=k 
    else:
        d1 = dist - d2
    p1 = p1 + (p2 - p1)*r1/dist
    p2 = p2 + (p1 - p2)*r2/dist
    rAngle = atan2(p2.y() - p1.y(),p2.x() - p1.x() ) % (2*pi)
    leftAngle = rAngle + pi/2
    rightAngle = leftAngle + pi
    leftPoint = pointAtAngle(leftAngle)
    rightPoint = pointAtAngle(rightAngle)
    headWidth = tan(theta/2)*d2 - pathWidth/2
    c = range(8)
    c[0] = p1
    c[1] = p1 + leftPoint*pathWidth/2
    c[2] = (p1 + (d1/dist)*(p2-p1)) + leftPoint*pathWidth/2
    c[3] = c[2] + leftPoint*headWidth
    c[4] = p2
    c[7] = p1 + rightPoint*pathWidth/2
    c[6] = (p1 + (d1/dist)*(p2-p1)) + rightPoint*pathWidth/2
    c[5] = c[6] + rightPoint*headWidth
    path.lineTo(c[1])
    path.lineTo(c[2])
    path.lineTo(c[3])
    path.lineTo(c[4])
    path.lineTo(c[5])
    path.lineTo(c[6])
    path.lineTo(c[7])
    path.lineTo(c[0])
    
    return path
