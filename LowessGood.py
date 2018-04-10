import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import datasets
import dataLowess

def euclidean(x,y):
    return np.sqrt(np.sum((x-y)**2))
    
def K(r): #gauss
     return( ((2* math.pi)**( -0.5)) * math.exp(-0.5*r*r) );

def det2(a,b,c,d):
    return a*d-b*c

def Solve(a,b,c,d,y1,y2):
    det = det2(a,b,c,d)
    d1 = det2(y1,b,y2,d)
    d2 = det2(a,y1,c,y2)
    return d1/det, d2/det
  
def getAB(X, Y, W):
    a = np.sum(X*X*W)
    b = np.sum(X*W)
    c = np.sum(X*W)
    d = np.sum(W)
    y1 = np.sum(X*W*Y)
    y2 = np.sum(W*Y)
    return(Solve (a,b,c,d,y1,y2))

def getArray(n):
    return np.zeros(n)
    
def lowess(X,Y,h, ro=euclidean):
    n = X.size
    ww = getArray(n)
    Yt = getArray(n)
    
    for step in range(2):
        #Yt = getArray(n)
        for i in range(n):
        
            for j in range(n):
                ww[j] = K(ro(X[i],X[j])/h)
            
            ret = getAB(X,Y,ww)
            
            Yt[i] = ret[0]*X[i] + ret[1]

    return Yt

X, Y = dataLowess.DataBuilder().Build("poisson")
# X, Y = dataLowess.DataBuilder().Build("wavelet")

h=0.5
Yt = lowess(X,Y,h)
print(Yt)

plt.plot(X, Yt, label='y pred', color = "pink")
plt.scatter(X,Y)
plt.show()
    
