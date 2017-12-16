import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import datasets
import data

def euclidean(x,y):
    return np.sqrt(np.sum((x-y)**2))

def K(r): #gauss
     return( ((2* math.pi)**( -0.5)) * math.exp(-0.5*r*r) );

def K1(r): #epanechnikov
    if -1 <= r and r <= 1 :
        return( 3/4 * (1-r*r) )
    else:
        return 0

def nadaray(X,Y, h=0.9, ro=euclidean):
    n = X.size
    Yt = np.zeros(n)
    for t in range(n):
        W = np.zeros(n)
        for i in range(n):
            W[i] = K(ro(X[t], X[i])/h)
        Yt[t] = sum(W*Y)/sum(W)
    return Yt
    
def lowess(X,Y, MAX=10, h=0.9, ro=euclidean):
    n = X.size
    delta = np.ones(n)
    Yt = np.zeros(n)
    
    for step in range (MAX):
        # print(delta)
        # print("")
        for t in range(n):
            W = np.zeros(n)
            for i in range(n):
                W[i] = delta[t]*K(ro(X[t], X[i])/h)
            Yt[t] = sum(W*Y)/sum(W)
            
        # print(Y)
        # print("")
        # print(Yt)
        # print("-----------------------")
        # print("")
        Q = np.fabs(Y-Yt)
        delta = [K1(Q[j]) for j in range(n)]
    return Yt


np.set_printoptions(formatter={'float':lambda x: '%.4f' % x})
X, Y = data.DataBuilder().Build("poisson")
#X, Y = data.DataBuilder().Build("wavelet")

Yt = nadaray(X,Y)
Yt1 = lowess(X,Y)
plt.scatter(X,Y)
plt.plot(X, Yt1, label='y pred', color = "orange")
plt.plot(X, Yt, label='y pred', color = "pink")
plt.show()

