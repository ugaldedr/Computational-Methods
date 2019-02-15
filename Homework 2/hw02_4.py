"""
   Name: Dario Ugalde
   MavID: 1001268068
   Course: CSE 4345 Computational Methods
"""

import numpy as np

print("//////////// Part a //////////")
print("     WITHOUT PERTURBATIONS:\n")

A = np.array([[0.1, 0.2, 0.3],
              [0.4, 0.5, 0.6],
              [0.7, 0.8, 0.91]])
b = np.array([[1.00],
              [2.80],
              [4.61]])

x = np.linalg.solve(A,b)
print("A =")
print(A)
print("\nb =")
print(b)
print("\nx =")
print(x)

print("\n     WITH PERTURBATIONS:\n")
b = np.array([[1.00],
              [2.80],
              [4.66]])

x = np.linalg.solve(A,b)
print("A = ")
print(A)
print("\nb =")
print(b)
print("\nx =")
print(x)
print("This part demonstrates how perturbations can create such\na significant impact on the solution of a system of equations.\nComparing the results of these two systems its very easy to\n see how the results more than doubled, even tripling for some cases, for x with the addition of perturbations.")

print("//////////// Part b //////////")
print("     WITHOUT PERTURBATIONS:")

A = np.array([[0.1, 0.2, 0.3],
              [0.6, 0.5, 0.4],
              [0.1, 0.5, -0.8]])
b = np.array([[1.0],
              [3.2],
              [0.5]])

x = np.linalg.solve(A,b)
print("A = ")
print(A)
print("\nb =")
print(b)
print("\nx =")
print(x)
print()

print("     WITH PERTURBATIONS:\n")
b = np.array([[1.0],
              [3.2],
              [1.0]])

x = np.linalg.solve(A,b)
print("A =")
print(A)
print("\nb =")
print(b)
print("\nx =")
print(x)

print("\nFor this part, the impact of the perturbations were not\nas significant as with part a. However it is important\nto note that for this system of equations perturbations\nstill have a noteworthy impact on the x values.")
