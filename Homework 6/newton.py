import numpy as np

x = np.array([1,-1])

for i in range(0,6):
    print("Iteration " + str(i))
    f = np.array([x[0]**2 - 2 * x[1]**2 + 14, 3 * x[0]**2 + x[1]**3 - 39])
    J = np.array([[2 * x[0], -4 * x[1]],[6 * x[0], 3 * x[1]**2]])
    s = np.linalg.solve(J,f)
    x = x - s
    print("f(x) = ")
    print(f)
    print()
    print("J(x) = ")
    print(J)
    print()
    print("s = ")
    print(s)
    print()
    print("x = ")
    print(x)
    print()
