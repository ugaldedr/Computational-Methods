import numpy as np
x = 3
f = x ** 2 - 3 * x - 5
f_hat = 2 * x - 3

i = 0
while i < 4:
    x = x - (f / f_hat)
    f = x ** 2 - 3 * x - 5
    f_hat = 2 * x - 3
    print("x_" + str(i + 1) + " : " + str(x))
    print("\tf(x) = " + str(f))
    print("\tf'(x) = " + str(f_hat))
    i = i  + 1
