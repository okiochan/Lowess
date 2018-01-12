import matplotlib.pyplot as plt
import numpy as np, json
from sklearn import datasets

def swirly():
    import sys
    sys.path.append(r"C:\Users\u\Documents\Python Scripts\NeuralNetwork")
    import matplotlib.pyplot as plt, numpy as np
    import random

    def shuffle(x, y):
        i = x.shape[0] - 1
        ret = np.zeros(i + 1, dtype=int)
        for k in range(i + 1):
            ret[k] = k
        while i > 0:
            j = random.randint(0, i)
            ret[i], ret[j] = ret[j], ret[i]
            i -= 1
        return ret

    np.random.seed(27182818)
    N = 100 # number of points per class
    D = 2 # dimensionality
    K = 6 # number of classes
    X = np.zeros((N*K,D)) # data matrix (each row = single example)
    y = np.zeros(N*K, dtype=float) # class labels
    pos = 0
    for j in range(K):
        r = np.linspace(0.1,1,N) # radius
        t = np.linspace(j*5.2,(j+1)*5.2,N) + np.random.randn(N)*0.2 # theta
        for l in range(r.size):
            X[pos] = np.c_[r[l]*np.sin(t[l]), r[l]*np.cos(t[l])]
            y[pos] = j
            pos += 1

    return X, y


def cool_data():
    from sklearn.ensemble import BaggingClassifier
    from sklearn.datasets import make_gaussian_quantiles
    from sklearn.svm import SVC

    np.random.seed(27182818)
    X1, y1 = make_gaussian_quantiles(cov=2.,
                                     n_samples=200, n_features=2,
                                     n_classes=2, random_state=1)
    X2, y2 = make_gaussian_quantiles(mean=(3, 3), cov=1.5,
                                     n_samples=300, n_features=2,
                                     n_classes=2, random_state=1)
    X = np.concatenate((X1, X2))
    y = np.concatenate((y1, - y2 + 1))
    return X, y

def normal(centerx, centery, disp, N):
    x = disp * np.random.randn(N) + centerx
    y = disp * np.random.randn(N) + centery
    return np.column_stack((x, y))

def gen(n, m, N):
    data = np.zeros((1, 3))
    np.random.seed(3)
    for i in range(n):
        for j in range(m):
            cls = np.ones(N) * (1 if ((i + j) % 2 == 0) else -1)
            tmp = normal(i, j, 1/5*1.5, N)
            tmp = np.column_stack((tmp, cls))
            data = np.row_stack((data, tmp))
    return data[1:,:]

def getData():
    # x1 = normal(-1, 0, 0.3, 10)
    # y1 = np.ones(x1.shape[0])
    # x2 = normal(1, 0, 0.3, 1)
    # y2 = np.ones(x2.shape[0]) * -1

    # Xl = np.vstack((x1,x2))
    # Yl = np.concatenate((y1,y2))

    # return Xl,Yl

    N = 50
    # ret = gen(2, 1, N)
    square = 4
    ret = gen(square,square, N)
    x, y = ret[:,:2], ret[:,2]
    return x, y

def display2DData(Xl, Yl):
    l = Xl.shape[0]
    plt.scatter(Xl[:,0], Xl[:,1], c=Yl, s=50)
    plt.show()

def plant_data():
    import csv

    X = []
    y = []
    with open('power_plant_data.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            if reader.line_num == 1: continue # skip header
            X.append([float(row[i].replace(',', '.')) for i in range(4)])
            y.append(float(row[4].replace(',', '.')))
    X = np.array(X)
    y = np.array(y)
    return X, y

class Data:
    def __init__(self):
        return

    def GetX(self):
        pass

    def GetY(self):
        pass

class SimpleData(Data):
    def __init__(self, X, y):
        Data.__init__(self)
        self.X = X
        self.y = y

    def GetX(self):
        return self.X

    def GetY(self):
        return self.y

class NormalizedData(Data):
    def __init__(self, data):
        Data.__init__(self)
        self.data = data

    def Normalized(self, arr):
        max_value = np.max(arr)
        min_value = np.min(arr)
        arr = (arr - min_value) / (max_value - min_value) * 2 - 1
        return arr

    def GetX(self):
        X = self.data.GetX()
        for i in range(X.shape[1]):
            X[...,i] = self.Normalized(X[...,i])
        return X

    def GetY(self):
        y = self.data.GetY()
        y = self.Normalized(y)
        return y

class DataFactory:
    def createData(self, name):
        if name == 'checkerboard':
            return getData()
        elif name == 'iris':
            iris = datasets.load_iris()
            return iris.data[:,[2,3]], iris.target
        elif name == '123':
            x = [
                [1, 2],
                [2, 2],
                [3, 2],
                [4, 2],
                [5, 2],
                [6, 2],
            ]
            y = [1, 1, 2, 2, 2, 2]
            x = np.array(x, dtype=float)
            x = np.atleast_2d(x)
            y = np.array(y, dtype=float)
            return x, y
        elif name == 'swirly':
            return swirly()
        elif name == 'cool':
            return cool_data()
        elif name == 'plant':
            X, y = plant_data()
            sd = SimpleData(X, y)
            nd = NormalizedData(sd)
            return nd
        elif name == 'plant_with_control':
            data = self.createData('plant')
            X, Y = data.GetX(), data.GetY()

            # shuffle
            cases = X.shape[0]
            np.random.seed(2718281828)
            perm = np.random.permutation(cases)
            X = X[perm,...]
            Y = Y[perm,...]

            take = (cases*9)//10
            X_train, Y_train = X[:take,...], Y[:take,...]
            X_control, Y_control = X[take:,...], Y[take:,...]
            return X_train, Y_train, X_control, Y_control
        else:
            assert 0

if __name__ == "__main__":
    X, y = DataFactory().createData('plant')
    print(X, y)
    # inp, out = DataFactory().createData('swirly')
    # display2DData(inp,out)

