import numpy as np


def Cramer(A, b):
    n = len(A)
    Di = [np.array(A) for i in range(n)]
    for i in range(n):
        Di[i][:, i] = b
    return [np.linalg.det(Di)[i] / np.linalg.det(A) for i in range(n)]


x = [[1, 0, 0],
     [0, 1, 0],
     [0, 0, 1]]

y = [1, 2, 3]
print(Cramer(x, y))
