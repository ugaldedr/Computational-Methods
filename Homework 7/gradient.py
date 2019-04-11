"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 4345 Computational Methods
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def positionHospital(c, h, alpha, tol) :
    k = 0
    locations = np.array([])
    locations = np.append(locations, h[0])
    locations = np.append(locations, h[1])
    point = np.array([0,0])
    while 1:
        sumSquared = 0
        gradient = np.array([0,0])
        for x in range(0,len(c)):
            row = c[x:x+1,:]
            i = row[:,0]
            j = row[:,1]
            i = i[0]
            j = j[0]
            sumSquared = sumSquared + (i - h[0])**2 + (j - h[1])**2
            gradient[0] = gradient[0] + (-1 * i + h[0])
            gradient[1] = gradient[1] + (-1 * j + h[1])
        gradient[0] = gradient[0] * -2
        gradient[1] = gradient[1] * -2
        point = h + (alpha * gradient)
        locations = np.append(locations, point[0])
        locations = np.append(locations, point[1])
        print("k = {0:2d}, fVal = {1: .2f}, grad = [{2: .2f}, {3: .2f}] h = [{4: .2f}, {5: .2f}]".format(k, sumSquared, gradient[0], gradient[1], point[0], point[1]))
        if np.linalg.norm(h - point) < tol:
            break
        h = point
        k = k + 1
    return locations
        

def plotCoor(cities, hospital) :
    plt.figure()
    plt.title("Cities and Hospital locations")
    for x in range(0,len(cities)):
        row = cities[x:x+1,:]
        i = row[:,0]
        j = row[:,1]
        i = i[0]
        j = j[0]
        plt.plot(i,j,'bo')
    for x in range(0,len(hospital),2):
        i = hospital[x]
        j = hospital[x + 1]
        plt.plot(i,j,'rx')
    plt.show()
        



###################  main  ###################
if __name__ == "__main__":
    #  coordinates of cities
    cities = np.array([[ 0,   0],
                       [30, 110],
                       [60, 100],
                       [50,  50]])
    
    #   initial coordinates of hospital
    hosp = np.array([0, 55])
    alpha = 0.01
    tol = 1
    
    hNew = positionHospital(cities, hosp, alpha, tol) 
    plotCoor(cities, hNew)
    
