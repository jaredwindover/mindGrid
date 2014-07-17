from math import sin, cos, atan2, degrees, pi, sqrt
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def ltIndex(i):
    def lti(a,b):
        if a[i] < b[i]:
            return a
        else:
            return b
    return lti

def norm(point):
    return sqrt(point.x()**2 + point.y()**2)

def dot(qp1,qp2):
    return qp1.x()*qp2.x() + qp1.y()*qp2.y()

def proj(qp1,qp2):
    m2 = norm(qp2)
    qp2hat = qp2/m2
    return dot(qp1,qp2hat)*qp2hat
    
def pointAtAngle(angle):
    return QPointF(cos(angle),sin(angle))
