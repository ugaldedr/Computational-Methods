"""
    Name: Dario Ugalde
    MavID: 1001268068
    Course: CSE 4345 Computational Methods
"""

import numpy as np
import matplotlib.pyplot as plt

table = open("circle-data.csv","r")
x_values = np.array([])
y_values = np.array([])
b = np.array([])

line = " "
while line is not "":
    line = table.readline()
    if line is "":
        break
    line = line[0:len(line) - 1]
    values = line.split(",")
    x_values = np.append(x_values,np.array([float(values[0])]))
    y_values = np.append(y_values,np.array([float(values[1])]))
    b = np.append(b,np.array([float(values[0]) ** 2 + float(values[1]) ** 2]))

x_values_2 = x_values * 2
y_values_2 = y_values * 2

A = np.c_[x_values_2,y_values_2,np.ones(len(x_values_2))]
b = np.c_[b]
least_square = np.linalg.lstsq(A,b,rcond = -1)
x = least_square[0]
residual = least_square[1]

h = x[0]
k = x[1]
r = x[2] - x[1] ** 2 - x[0] ** 2
r = r ** (1/2)

print("h: ",h," k: ",k," r: ",r)

fig=plt.figure(1)
ax=fig.add_subplot(1,1,1)
plt.plot(x_values,y_values,'bo')
plt.plot(h,k,'yx')
Circ = plt.Circle((h,k),radius = r, color = 'g', fill = False)
ax.add_patch(Circ)
plt.axis([-30,30,-20,25])
plt.show()
