import numpy as np

x = np.array([-2,1])

for i in range(0,4):
    print("iteration {0:d}".format(i))
    print("x = ")
    print(x)
    H_f = np.array([[6 * x[0], -1], [-1, 6 * x[1]]])
    print("Hessian = ")
    print(H_f)
    gradient = np.array([3 * x[0]**2 - x[1], 3 * x[1]**2 - x[0]])
    print("Gradient = ")
    print(gradient)
    s = np.linalg.solve(H_f,gradient)
    print("s = ")
    print(s)
    x = x + s
    print("x_{0:d} = ".format(i+1))
    print(x)
    print("---------------------------------")
f = x[0]**3 - x[0] * x[1] + x[1]**3
print()
print("f = ")
print(f)
H_f = np.array([[6 * x[0], -1], [-1, 6 * x[1]]])
print("Hessian of x_4 =")
print(H_f)
print()
print("------------- Pulled values to answer questions -----------------")
print(H_f[0,0]*H_f[1,1])
print(H_f[0,0]*2)
