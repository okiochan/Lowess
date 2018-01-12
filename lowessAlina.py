import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import datasets
import dataLowess
import matplotlib.patches as mpatches

def generate(n_support=1000, n_train=30, std=0.5):
    data = {}
    # выберем некоторое количество точек из промежутка от 0 до 2*pi
    data['support'] = np.linspace(0, 2*np.pi, num=n_support)
    # для каждой посчитаем значение cos(x) + 1
    # это будет ground truth
    data['values'] = np.cos(data['support']) + 1
    # из support посемплируем некоторое количество точек с возвратом, это будут признаки
    data['x_train'] = np.sort(np.random.choice(data['support'], size=n_train, replace=True))
    # опять посчитаем cos(x) + 1 и добавим шум, получим целевую переменную
    data['y_train'] = np.cos(data['x_train']) + 1 + np.random.normal(0, std, size=data['x_train'].shape[0])
    X = data['x_train'] 
    Y = data['y_train']
    return X, Y

def euclidean(x,y):
    return np.sqrt(np.sum((x-y)**2))

def Kgauss(r): #gauss yadro
     return( ((2* math.pi)**( -0.5)) * math.exp(-0.5*r*r) );

def Kquad(r): #qwadratic yadro
    if (abs(r) <= 1):
        return (1-r*r)*(1-r*r)
    else:
        return 0

def Error(Y, Yt):
    l = Y.shape[0]
    err = ((Yt-Y)**2).sum()/l
    return err
   
def nadaray(X,Y, h, K, ro=euclidean):
    n = X.size
    Yt = np.zeros(n)
    for t in range(n):
        W = np.zeros(n)
        for i in range(n):
            W[i] = K(ro(X[t], X[i])/h)
        wsum = 0
        for i in range(n):
            Yt[t] += W[i]*Y[i]
            wsum += W[i]
        Yt[t] /= wsum
    return Yt

def lowess(X,Y, MAX, h, K, K1, ro=euclidean):
    n = X.shape[0]
    gamma = np.ones(n)
    Yt = np.zeros(n)
    
    for step in range (MAX):
        w = []
        for t in range(n):
            w.append([])
            for i in range(n):
                w[t].append(K(ro(X[i], X[t]) / h)*gamma[t])
                
        w = np.array(w)
        Yt = (w * Y[:, None]).sum(axis=0) / w.sum(axis=0)
    
        Q = np.abs(Y-Yt)
        gamma = [K1(Q[j]) for j in range(n)]
        gamma = np.array(gamma,dtype=float)
    return Yt

X, Y = generate()

np.set_printoptions(formatter={'float':lambda x: '%.4f' % x})

Yt1 = lowess(X,Y,MAX=2, h=0.6, K=Kgauss, K1 = Kquad)
Yt2 = nadaray(X,Y, h=0.6, K=Kgauss)
Yt3 = nadaray(X,Y, h=0.6, K=Kquad)

print("Lowess")
print(Error(Y, Yt1))
print("Nadaray with gauss")
print(Error(Y, Yt2))
print("Nadaray with qwadratic")
print(Error(Y, Yt3))


plt.scatter(X,Y)
plt.plot(X, Yt1, label='y pred', color = "orange")
plt.plot(X, Yt2, label='y pred', color = "pink")
#plt.plot(X, Yt3, label='y pred', color = "red")

plt.legend(handles=[mpatches.Patch(color='orange', label='Lowess'),mpatches.Patch(color='pink', label='Nadaray-Watson')])
# plt.legend(handles=[mpatches.Patch(color='red', label='Nadaray-Watson with K quadratic'),mpatches.Patch(color='pink', label='Nadaray-Watson with K gauss')])
plt.show()