import math
from datetime import datetime


def f(x):
    return 3 ** x - 2 * x + 5


a = float(input('Enter a: '))
b = float(input('Enter b: '))
# for the precision of the root
z = float(input('Enter the significant digit: '))

E = 10 ** (-z)
# Formula for the number of iterations
n = (math.log(b - a) - math.log(E)) / math.log(2)
n = math.ceil(n)

print('The number of iterations is: ', n)
# t_i = datetime.now()
i = 0
while i < n:
    r = (a+b)/2
    err = abs(r - a)
    print(f'at iteration app. root is: {r}, errotr is {err}')
    if (f(a) * f(r) < 0):
        b = r
    elif (f(b) * f(r) < 0):
        a = r
    i += 1
