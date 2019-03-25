import numpy as np

a = 1
b = 2
m = 0

x = 0
while x < 4:
    print("Iteration " + str(x + 1) + ":")
    m = a + (b - a) / 2
    print("\tm = " + str(m))
    if (m ** 3 - 4) < 0:
        a = m
    else:
        b = m
    x = x + 1
    print("\ta = " + str(a) + "\n\tb = " + str(b) + "\n")

print("Approximate Root: " + str(a + (b - a) / 2))
