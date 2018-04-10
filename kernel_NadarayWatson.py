import numpy as np
from scipy.spatial import distance
import pylab as pl

h = 0.5
eps = 1e-5


# Gauss kernel
def kernel(z):
    return (1.0 / np.sqrt(2 * np.pi)) * np.exp(- 0.5 * z ** 2)

# Kvartich kernel
def kernel_gamma(z):
    if (abs(z) <= 1):
        return (1-z**2)**2
    else:
        return 0


def stability(arr):
    for el in arr:
        if el > eps:
            return True
    return False


def nadaray_watson(x, y):
    n = len(x)
    w = []
    for t in range(n):
        w.append([])
        for i in range(n):
            w[t].append(kernel(distance.euclidean(x[t], x[i]) / h))
    w = np.array(w)
    yest = (w * y[:, None]).sum(axis=0) / w.sum(axis=0)
    return yest

def lowess(x, y):
    n = len(x)

    gamma = np.ones(n)
    gamma_old = np.zeros(n)
    yest = np.zeros(n)
    cnt = 0

    while stability(np.abs(gamma - gamma_old)):
        cnt += 1
        w = []
        for t in range(n):
            w.append([])
            for i in range(n):
                w[t].append(kernel(distance.euclidean(x[t], x[i]) / h)*gamma[t])
        w = np.array(w)
        yest = (w * y[:, None]).sum(axis=0) / w.sum(axis=0)

        err = np.abs(yest - y)
        gamma = [kernel_gamma(err[j]) for j in range(n)]
        if (cnt > 5):
            break
    return yest

def generate_wave_set(n_support=1000, n_train=250):
    data = {}
    data['support'] = np.linspace(0, 2 * np.pi, num=n_support)
    data['x_train'] = np.sort(np.random.choice(data['support'], size=n_train, replace=True))
    data['y_train'] = np.sin(data['x_train']).ravel()
    data['y_train'] += 0.5 * (0.55 - np.random.rand(data['y_train'].size))
    return data


if __name__ == '__main__':
    data = generate_wave_set(100, 80)
    x = data['x_train']
    y = data['y_train']
    # x = [0.25386607, 0.38079911, 0.44426563, 0.50773215, 0.63466518, 0.6981317,
    #      0.6981317, 0.76159822, 0.82506474, 0.88853126, 1.01546429, 1.01546429,
    #      1.07893081, 1.07893081, 1.20586385, 1.20586385, 1.20586385, 1.33279688,
    #      1.3962634, 1.45972992, 1.52319644, 1.58666296, 1.58666296, 1.58666296,
    #      1.65012947, 1.77706251, 1.84052903, 2.0943951, 2.15786162, 2.28479466,
    #      2.28479466, 2.34826118, 2.60212725, 2.66559377, 2.72906028, 2.7925268,
    #      2.85599332, 2.91945984, 2.98292636, 3.04639288, 3.17332591, 3.36372547,
    #      3.36372547, 3.42719199, 3.74452458, 3.74452458, 3.8079911, 3.87145761,
    #      3.87145761, 3.93492413, 3.93492413, 4.12532369, 4.12532369, 4.25225672,
    #      4.25225672, 4.44265628, 4.44265628, 4.75998887, 4.75998887, 4.88692191,
    #      4.95038842, 5.01385494, 5.07732146, 5.14078798, 5.14078798, 5.2042545,
    #      5.26772102, 5.26772102, 5.26772102, 5.33118753, 5.33118753, 5.39465405,
    #      5.45812057, 5.58505361, 5.77545316, 5.9023862, 5.9023862, 6.02931923,
    #      6.02931923, 6.09278575]
    # x = np.array(x)
    # y = [0.49982011, 0.63374955, 0.53061878, 0.59367792, 0.45592541, 0.61205114,
    #      0.71930172, 0.92626773, 0.8657404, 1.02649539, 0.73206656, 0.90497831,
    #      0.69356384, 0.78491523, 0.97736607, 0.86285144, 1.20904129, 0.7576733,
    #      0.914767, 0.86502363, 1.04857959, 0.97525585, 0.91044818, 1.02938393,
    #      0.89784696, 1.1240391, 0.80756406, 0.66134528, 1.07807525, 0.80300803,
    #      0.98238924, 0.74657294, 0.44939097, 0.27385452, 0.51173434, 0.60492519,
    #      0.34246772, 0.44536315, 0.2113706, 0.21893242, -0.22776609, -0.24373031,
    #      -0.27342691, -0.40625428, -0.57759724, -0.36327529, -0.68233917, -0.54106024,
    #      -0.594002, -0.54278992, -0.72141841, -0.84960626, -0.99065906, -0.95052521,
    #      -0.77855943, -1.1411366, -0.82951384, -0.98987168, -0.73749955, -1.03039024,
    #      -0.87363562, -0.96550525, -0.78238156, -1.02137395, -0.89266227, -0.9028713,
    #      -0.7883536, -0.72666741, -1.04589251, -0.73791169, -0.71817151, -0.64454691,
    #      -0.50123652, -0.73558315, -0.3898374, -0.40887712, -0.25264427, -0.02445753,
    #      -0.44606617, -0.16614301]
    # y = np.array(y)

    # # x = [[1], [2], [3], [4], [5]]
    # x = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12]]
    # x = np.array(x)
    # # y = [1, 2, 4, 3, 2]
    # y = [1, 2, 4.3, 3, 2, 2, 1.5, 1.3, 1.5, 1.7, 1.8, 2]
    # y = np.array(y)

    print("Nadaray Watson's yest:")
    yest_nadaray = nadaray_watson(x, y)
    print(yest_nadaray)
    print("Lowess yest:")
    yest_lowess = lowess(x, y)
    print(yest_lowess)

    pl.clf()
    pl.scatter(x, y, label='data', color="black")
    pl.plot(x, yest_nadaray, label='y nadaray-watson', color="red")
    pl.plot(x, yest_lowess, label='y lowess', color="blue")
    pl.title('Nadaray Watson vs Lowess')
    pl.legend()
    pl.show()
