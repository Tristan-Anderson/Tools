import numpy as np
import sys

def newx(l, theta):
    x1, y1 = l
    return np.cos(theta)*x1 + np.sin(theta)*y1

def newy(l, theta):
    x1,y1=l
    return -np.sin(theta)*x1+np.cos(theta)*y1

def diff2v(v1,v2):
    x1,y1=v1
    x2,y2=v2
    return [x1-x2,y1-y2]

def add2v(v1,v2):
    x1,y1=v1
    x2,y2=v2
    return [x1+x2,y1+y2]



def main(x1,y1,t, ox1=40, oy1=40):
    origin = [ox1, oy1]
    absv = [x1,y1]
    theta = t * np.pi/180

    l = diff2v(absv, origin)

    newv_r = [newx(l,theta), newy(l,theta)]
    newv = add2v(newv_r, origin)


    relv = diff2v(newv,absv)
    print("new vector", end=' ')
    print([round(i,5) for i in newv])
    print("relative vector",end=" ")
    print([round(i,5) for i in relv])
    return True
a = sys.argv[1:]
print(a)
print(np.pi)
try:
    main(float(a[0]),float(a[1]),float(a[2]))
except IndexError:
    print("Did not recieve all arguments.")
