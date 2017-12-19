import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import datasets
import data

def euclidean(x,y):
    return np.sqrt(np.sum((x-y)**2))

def K(r): #gauss
     return( ((2* math.pi)**( -0.5)) * math.exp(-0.5*r*r) );

def K1(z):
    if (abs(z) <= 1):
        return (1-z**2)**2
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

def lowess(X,Y, MAX=2, h=0.9, ro=euclidean):
    n = X.size
    delta = np.ones(n)
    Yt = np.zeros(n)
    fudge = 1e-5
    for step in range (MAX):
        for t in range(n):
            num = 0
            den = 0
            for i in range(n):
                # if i == t:continue
                num += Y[i] * delta[i] * K(ro(X[i], X[t]) / h)
                den += delta[i] * K(ro(X[i], X[t]) / h)
            Yt[t] = num / den
            # W = np.empty(n)
            # for i in range(n):
                # W[i] = delta[t]*K(ro(X[t], X[i])/h)
            # print(W)
            # Yt[t] = np.sum(W*Y)/(np.sum(W) + fudge)

        print(Yt)
        Q = np.abs(Y-Yt)
        delta = [K1(Q[j]) for j in range(n)]
        delta = np.array(delta,dtype=float)
        print()
    return Yt


# X, Y = data.DataBuilder().Build("poisson")
# X, Y = data.DataBuilder().Build("wavelet")
X, Y = data.DataBuilder().Build("degenerate")

np.set_printoptions(formatter={'float':lambda x: '%.4f' % x})
Yt2 = nadaray(X,Y)
Yt1 = lowess(X,Y)
plt.scatter(X,Y)
plt.plot(X, Yt1, label='y pred', color = "orange")
plt.plot(X, Yt2, label='y pred', color = "pink")
plt.show()
