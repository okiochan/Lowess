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

def alpha(id,X,Y, delta,h, ro=euclidean):
    m = X.size
    sum1 = 0
    for i in range(m):
        if id == i:
            continue
        sum1 += Y[i]*delta[i]*K(ro(X[id], X[i])/h)
    sum2 = 0
    for i in range(m):
        if id == i:
            continue
        sum2 += K(ro(X[id], X[i])/h)
    return sum1/sum2

def GetArray(n):
    return np.ones(n)

def lowess(X, Y):
    n = X.size
    delta = GetArray(n)
    delta1 = GetArray(n)
    Yt = GetArray(n)
    h = 0.06
    EPS = 1e-8

    for step in range(100000):

        print(step)

        for t in range(n):
            Yt[t] = alpha(t,X,Y, delta,h)
            E = math.fabs(Yt[t] - Y[t])
            delta1[t] = K1(E)

        maxv = 0
        for i in range(n) :
            maxv = max(maxv, math.fabs(delta[i] - delta1[i]) )
            delta[i] = delta1[i]

        if maxv < EPS :
            break

    plt.plot(X, Yt, label='y pred', color = "pink")

# X, Y = data.DataBuilder().Build("poisson")
X, Y = data.DataBuilder().Build("wavelet")

lowess(X,Y)
print(X,Y)
plt.scatter(X,Y)
plt.show()

