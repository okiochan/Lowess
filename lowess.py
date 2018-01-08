import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import datasets
import dataLowess
import matplotlib.patches as mpatches

def euclidean(x,y):
    return np.sqrt(np.sum((x-y)**2))

def Kgauss(r): #gauss yadro
     return( ((2* math.pi)**( -0.5)) * math.exp(-0.5*r*r) );

def Kquad(r): #qwadratic yadro
    if (abs(r) <= 1):
        return (1-r**2)**2
    else:
        return 0

def QuadraticError(Y, Yt):
    return ((Yt-Y)**2).sum()
   
def nadaray(X,Y, h, K, ro=euclidean,):
    n = X.size
    Yt = np.zeros(n)
    for t in range(n):
        W = np.zeros(n)
        for i in range(n):
            W[i] = K(ro(X[t], X[i])/h)
        Yt[t] = sum(W*Y)/sum(W)
    return Yt

def lowess(X,Y, MAX, h, K, K1, ro=euclidean):
    n = X.size
    delta = np.ones(n)
    Yt = np.zeros(n)
    fudge = 1e-5
    for step in range (MAX):
        for t in range(n):
            num = 0
            den = 0
            for i in range(n):
                num += Y[i] * delta[i] * K(ro(X[i], X[t]) / h)
                den += delta[i] * K(ro(X[i], X[t]) / h)
            Yt[t] = num / den

        Q = np.abs(Y-Yt)
        delta = [K1(Q[j]) for j in range(n)]
        delta = np.array(delta,dtype=float)
    return Yt


X, Y = dataLowess.DataBuilder().Build("poisson")
# X, Y = dataLowess.DataBuilder().Build("wavelet")
#X, Y = dataLowess.DataBuilder().Build("degenerate")

np.set_printoptions(formatter={'float':lambda x: '%.4f' % x})

Yt1 = lowess(X,Y,MAX=2, h=0.6, K=Kgauss, K1 = Kquad)
Yt2 = nadaray(X,Y, h=0.6, K=Kgauss)
Yt3 = nadaray(X,Y, h=0.6, K=Kquad)

# print("Lowess")
# print(QuadraticError(Y, Yt1))
print("Nadaray with gauss")
print(QuadraticError(Y, Yt2))

print("Nadaray with qwadratic")
print(QuadraticError(Y, Yt3))


plt.scatter(X,Y)
# plt.plot(X, Yt1, label='y pred', color = "orange")
plt.plot(X, Yt2, label='y pred', color = "pink")
plt.plot(X, Yt3, label='y pred', color = "red")

# plt.legend(handles=[mpatches.Patch(color='orange', label='Lowess'),mpatches.Patch(color='pink', label='Nadaray-Watson')])
plt.legend(handles=[mpatches.Patch(color='red', label='Nadaray-Watson with K quadratic'),mpatches.Patch(color='pink', label='Nadaray-Watson with K gauss')])
plt.show()