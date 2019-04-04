"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 4345 Computational Methods
"""

import numpy as np
import math 


def positioning(alpha, beta, d1, d2, p1, p2):
    x = np.array([alpha,beta])
    print("Step {0:d}\t alpha = {1: .5f} \tbeta = {2: .5f}".format(0,x[0],x[1]))
    for i in range(0,6):
        equationOne = d1 * np.cos(alpha) + d2 * (np.cos(alpha)*np.cos(beta) - np.sin(alpha)*np.sin(beta)) - p1
        equationTwo = d1 * np.sin(alpha) + d2 * (np.sin(alpha)*np.cos(beta) + np.cos(alpha)*np.sin(beta)) - p2
        f = np.array([equationOne,equationTwo])
        J = np.array([[-d1 * np.sin(alpha) - d2 *(np.sin(alpha)*np.cos(beta) + np.cos(alpha)*np.sin(beta)), -d2 * (np.sin(alpha)*np.cos(beta) + np.cos(alpha)*np.sin(beta))],[d1 * np.cos(alpha) + d2 * (np.cos(alpha)*np.cos(beta) - np.sin(alpha)*np.sin(beta)), d2 * (np.cos(alpha)*np.cos(beta) - np.sin(alpha)*np.sin(beta))]])
        s = np.linalg.solve(J,f)
        x = x - s
        alpha = x[0]
        beta = x[1]
        print("Step {0:d}\t alpha = {1: .5f} \tbeta = {2: .5f}".format(i+1,x[0],x[1]))

##############  main  ##############
if __name__ == "__main__":
    #positioning(0.7, 0.7, 5, 6, 10, 4)
    positioning(0.7, 0.7, math.sqrt(29), math.sqrt(10), 6, 5)
