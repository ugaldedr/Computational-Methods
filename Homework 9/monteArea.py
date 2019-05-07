"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 4345 Computational Methods
"""

import numpy as np
import matplotlib.pyplot as plt
from random import uniform

def estArea(samples) :
    count = 0
    plt.figure()
    plt.xlim(0,11)
    plt.ylim(0,10)
    for i in range(0,samples):
        x = getX()
        y = getY()
        a = 2 * x - y
        b = 1/7 * x - y
        c = 1/6 * x + y
        if (a > 2):
            if(a < 15): 
                if(b < -12/7): 
                    if(c < 20/3) :
                        plt.plot(x,y,'bo')
                        count = count + 1
    area = 32 * count / samples
    print("Estimated area: {0:.2f}".format(area))
    print("Actual area: "+ str(19.5))
    plt.show()   
    
def getX():
    value = uniform(2,10)
    return value 

def getY():
    value = uniform(2,6)
    return value


########################  main  ########################
if __name__ == "__main__" :
    samples = 10000

    estArea(samples)

