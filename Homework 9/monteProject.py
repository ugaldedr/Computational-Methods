"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 4345 Computational Methods
"""

import numpy as np
from random import uniform

def estDuration(runs) :
    sum = 0
    min = 0
    max = 0
    for x in range(0,runs):
        current = 0
        A = taskA()
        B = taskB()
        C = taskC()
        D = taskD()
        current = A + B + C + D
        if min is 0:
            min = current
        if min > current:
            min = current
        if max < current:
            max = current
        sum = sum + current
    sum = sum / runs
    return min, max, sum
    
def taskA():
    probability = uniform(0,1)
    if 0 <= probability <= 0.1:
        return 2
    if 0.1 < probability <= 0.2:
        return 4
    return 3

def taskB():
    probability = uniform(0,1)
    if 0 <= probability < 0.5:
        return 1
    return 2

def taskC():
    probability = uniform(0,1)
    if 0 <= probability < 0.2:
        return 5
    if 0.2 <= probability < 0.4:
        return 8
    return 6

def taskD():
    probability = uniform(0,1)
    if 0 <= probability < 0.05:
        return 2
    if 0.05 <= probability < 0.1:
        return 3
    if 0.1 <= probability < 0.2:
        return 5
    return 4
    

########################  main  ########################
if __name__ == "__main__" :
    runs = 1000

    minDays, maxDays, avg = estDuration(runs)

    print("min = %d, max = %d, average = %.1f" % (minDays, maxDays, avg))

