"""
    Name:   Dario Ugalde
    Mav ID: 1001268068
    Course: CSE 4345 Computational Methods
"""

import numpy as np
import pandas as pd

"""
    Pull data from csv file and split into A and b
"""

data = pd.read_csv("svd-data.csv")
data = data.values
A = data[:,0:len(data[0]) - 1]
b = data[:,len(data[0]) -1:len(data[0])]

"""
    Solve for x and the residual vector
"""

A_t = A.transpose()
AtA = np.dot(A_t,A)
AtA_I = np.linalg.inv(AtA)
Atb = np.dot(A_t,b)

x = np.dot(AtA_I,Atb)
print("x = ")
print(x)

b_hat = np.dot(A,x)
r = b - b_hat
print()
print("The 2-norm of the residual vector: " + str(np.linalg.norm(r,2)))

"""
    Solve the system of linear equations and find the residual vector
"""

x_2 = np.linalg.solve(AtA,Atb)
print()
print("x = ")
print(x_2)

b_hat_2 = np.dot(A,x_2)
r_2 = b - b_hat_2
print()
print("The 2-norm of the residual vector: " + str(np.linalg.norm(r_2,2)))

"""
    Produce the SVD of A
"""

U,S,V = np.linalg.svd(A)
print()
print("The singular values of A:")
print(S.reshape(-1,1))

"""
    Find the effective rank of A
"""

rank = 0
i = 0
while i < len(S):
    if S[i] >= 0.1:
        rank = rank + 1
    i = i + 1
print()
print("The effective rank of A is " + str(rank))

"""
    Solve for x using the summation provided
"""
x_3 = np.zeros(len(x))

i = 1
while i <= rank:
    u = U[:,i]
    u = u.transpose()
    ub = np.dot(u,b) / S[i]
    x_3 = np.add(np.multiply(ub,V[:,i]), x_3)
    i = i + 1

print()
print("x = ")
print(x_3.reshape(-1,1))

"""
    Solve for the residual vector
"""

b_hat_3 = np.dot(A,x_3)
r_3 = b - b_hat_3

print()
print("The 2-norm of the residual vector is " + str(np.linalg.norm(r_3,2)))

"""
    Print the condition number
"""

cond = np.linalg.norm(AtA, 2)
print()
print("The condition number of AtA is " + str(cond))

"""
    Part D:
        The reason such a wide variety of b vectors are produced
        is because the data provided in the csv file is an
        overdetermined system of equations. In other words, 
        there are more equations than there are variables. This
        can lead to inconsistent results when applying different
        x vectors to the A matrix and is what we experience 
        through the course of this assignment.
"""
