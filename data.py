import matplotlib.pyplot as plt
import numpy as np
import scipy.misc
import math
from sklearn import datasets

class PoissonData:
    def Poisson(self, x):
        return -(-x*x) * np.exp(-x)

    def GetData(self, n):
        x = np.linspace(0,10,n)
        y = np.zeros(x.size)
        for i in range(x.size):
            y[i] = self.Poisson(x[i])

        # add noise
        np.random.seed(123123)
        y = y + np.random.randn(x.size) * 0.02
        return x, y

class WaveletData:
    def generate_wave_set(self, n_support=1000, n_train=25, std=0.3):
        data = {}
        # выберем некоторое количество точек из промежутка от 0 до 2*pi
        data['support'] = np.linspace(0, 2*np.pi, num=n_support)
        # для каждой посчитаем значение sin(x) + 1
        # это будет ground truth
        data['values'] = np.sin(data['support']) + 1
        # из support посемплируем некоторое количество точек с возвратом, это будут признаки
        data['x_train'] = np.sort(np.random.choice(data['support'], size=n_train, replace=True))
        # опять посчитаем sin(x) + 1 и добавим шум, получим целевую переменную
        data['y_train'] = np.sin(data['x_train']) + 1 + np.random.normal(0, std, size=data['x_train'].shape[0])
        X = data['x_train'] 
        Y = data['y_train']
        return X, Y

class DataBuilder:
    def Build(self, name):
        if name == "wavelet":
            x, y = WaveletData().generate_wave_set()
            return x, y
        elif name == "poisson":
            x, y = PoissonData().GetData(100)
            return x, y
        else:
            assert("Unknown data")

if __name__ == "__main__":
    x, y = DataBuilder().Build("wavelet")
    plt.scatter(x,y)
    plt.show()