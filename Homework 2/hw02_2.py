"""
    Name: Dario Ugalde
    MavID: 1001268068
    Course: CSE 4345
"""

import numpy as np

x = np.array([0.1,0.3,0.2])
x = np.transpose(x)

y = np.array([1.1,0.3,2.2])
y = np.transpose(y)

x_norm = np.linalg.norm(x)
y_norm = np.linalg.norm(y)

print("The norm of x without perturbations is: ",x_norm)
print("The norm of x with perturbations is: ",y_norm)
print("\nThe relative change in the norms is: ", (y_norm - x_norm) / x_norm)
