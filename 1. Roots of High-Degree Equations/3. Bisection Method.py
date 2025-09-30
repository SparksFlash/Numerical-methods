import math
from datetime import datetime


def f(x):
    return x ** 3 - 3 * x + 5


a = float(input('Enter a: '))
b = float(input('Enter b: '))
# for the precision of the root
z = float(input('Enter the significant digit: '))

E = 10 ** (-z)
# Formula for the number of iterations
n = (math.log(abs(b - a) - math.log(E))) / math.log(2)
n = math.ceil(n)

print('The number of iterations is: ', n)
# t_i = datetime.now()
i = 0
while i < n:
    root = (a + b) / 2
    err = abs(root - a)
    print(f'at iteration {i+1} app. root is: {root}, error is {err}')
    if (f(a) * f(root) < 0):
        b = root
    elif (f(b) * f(root) < 0):
        a = root
    i += 1
