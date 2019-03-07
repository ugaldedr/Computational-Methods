"""
    Name:   Dario Ugalde
    Mav ID: 1001268068
    Course: CSE 4345 Computational Methods
"""

import numpy as np

"""
    Pulling data from CSV files
"""
train = open("digitsTrainCombined.csv","r")
test = open("digitsTestCombined.csv","r")

training_data = np.empty((4000,), float)
test_data = np.empty((1000,), float)

line = " "
while line is not "":
    line = train.readline()
    if line is "":
        break
    line = line[0:len(line)-1]
    line = line.split(",")
    data = np.array([])
    for x in line:
        data = np.append(data, np.array([float(x)]))
    training_data = np.vstack((training_data, data))
training_data = np.delete(training_data,0,0)

line = " "
while line is not "":
    line = test.readline()
    if line is "":
        break
    line = line[0:len(line)-1]
    line = line.split(",")
    data = np.array([])
    for x in line:
        data = np.append(data,np.array([float(x)]))
    test_data = np.vstack((test_data, data))
test_data = np.delete(test_data,0,0)

"""
    Creating and nxq training matrices for each class
"""
zero = training_data[0:256,0:399]
one = training_data[0:256,400:799]
two = training_data[0:256,800:1199]
three = training_data[0:256,1200:1599]
four = training_data[0:256,1600:1999]
five = training_data[0:256,2000:2399]
six = training_data[0:256,2400:2799]
seven = training_data[0:256,2800:3199]
eight = training_data[0:256,3200:3599]
nine = training_data[0:256,3600:3999]

"""
    Calculating 2-norms for each test class at each k when k = 1, 5, 20, 100, 256
"""

k = np.array([1, 5, 20, 100, 256])
identity = np.identity(256)

for x in k:
    print("-------------------- k = " + str(x) + " --------------------")
    totalRight = 0
    totalWrong = 0
    right = 0
    wrong = 0

    U_k_zero,s,vh = np.linalg.svd(zero)
    U_k_zero = U_k_zero[0:256,0:x]
    U_k_T_zero = U_k_zero.transpose()
    firstHalf_zero = identity - np.dot(U_k_zero,U_k_T_zero)
    
    U_k_one,s,vh = np.linalg.svd(one)
    U_k_one = U_k_one[0:256,0:x]
    U_k_T_one = U_k_one.transpose()
    firstHalf_one = identity - np.dot(U_k_one,U_k_T_one)

    U_k_two,s,vh = np.linalg.svd(two)
    U_k_two = U_k_two[0:256,0:x]
    U_k_T_two = U_k_two.transpose()
    firstHalf_two = identity - np.dot(U_k_two,U_k_T_two)

    U_k_three,s,vh = np.linalg.svd(three)
    U_k_three = U_k_three[0:256,0:x]
    U_k_T_three = U_k_three.transpose()
    firstHalf_three = identity - np.dot(U_k_three,U_k_T_three)

    U_k_four,s,vh = np.linalg.svd(four)
    U_k_four = U_k_four[0:256,0:x]
    U_k_T_four = U_k_four.transpose()
    firstHalf_four = identity - np.dot(U_k_four,U_k_T_four)

    U_k_five,s,vh = np.linalg.svd(five)
    U_k_five = U_k_five[0:256,0:x]
    U_k_T_five = U_k_five.transpose()
    firstHalf_five = identity - np.dot(U_k_five,U_k_T_five)

    U_k_six,s,vh = np.linalg.svd(six)
    U_k_six = U_k_six[0:256,0:x]
    U_k_T_six = U_k_six.transpose()
    firstHalf_six = identity - np.dot(U_k_six,U_k_T_six)

    U_k_seven,s,vh = np.linalg.svd(seven)
    U_k_seven = U_k_seven[0:256,0:x]
    U_k_T_seven = U_k_seven.transpose()
    firstHalf_seven = identity - np.dot(U_k_seven,U_k_T_seven)

    U_k_eight,s,vh = np.linalg.svd(eight)
    U_k_eight = U_k_eight[0:256,0:x]
    U_k_T_eight = U_k_eight.transpose()
    firstHalf_eight = identity - np.dot(U_k_eight,U_k_T_eight)

    U_k_nine,s,vh = np.linalg.svd(nine)
    U_k_nine = U_k_nine[0:256,0:x]
    U_k_T_nine = U_k_nine.transpose()
    firstHalf_nine = identity - np.dot(U_k_nine,U_k_T_nine)

    y = 0
    while y < len(test_data[0]):
        testColumn = test_data[:,y]
        testColumn = np.column_stack((testColumn,))
        solution = 0
        currentTestCase = 10
        lowestNorm = 256
        z = 0
        while z < currentTestCase:
            if z is 0:
                calc = np.linalg.norm(np.dot(firstHalf_zero,testColumn), 2)
            if z is 1:
                calc = np.linalg.norm(np.dot(firstHalf_one,testColumn), 2)
            if z is 2:
                calc = np.linalg.norm(np.dot(firstHalf_two,testColumn), 2)
            if z is 3:
                calc = np.linalg.norm(np.dot(firstHalf_three,testColumn), 2)
            if z is 4:
                calc = np.linalg.norm(np.dot(firstHalf_four,testColumn), 2)
            if z is 5:
                calc = np.linalg.norm(np.dot(firstHalf_five,testColumn), 2)
            if z is 6:
                calc = np.linalg.norm(np.dot(firstHalf_six,testColumn), 2)
            if z is 7:
                calc = np.linalg.norm(np.dot(firstHalf_seven,testColumn), 2)
            if z is 8:
                calc = np.linalg.norm(np.dot(firstHalf_eight,testColumn), 2)
            if z is 9:
                calc = np.linalg.norm(np.dot(firstHalf_nine,testColumn), 2)

            if calc < lowestNorm:
                lowestNorm = calc
                solution = z  
            z = z + 1

        if y <= 99 and y >=0 and solution is 0:
            right = right + 1
            totalRight = totalRight + 1
            
        elif y >= 100 and y <=199 and solution is 1:
            right = right + 1
            totalRight = totalRight + 1
            
        elif y >= 200 and y <=299 and solution is 2:
            right = right + 1
            totalRight = totalRight + 1
            
        elif y >= 300 and y <=399 and solution is 3:
            right = right + 1
            totalRight = totalRight + 1
            
        elif y >= 400 and y <=499 and solution is 4:
            right = right + 1
            totalRight = totalRight + 1
            
        elif y >= 500 and y <=599 and solution is 5:
            right = right + 1
            totalRight = totalRight + 1
            
        elif y >= 600 and y <=699 and solution is 6:
            right = right + 1
            totalRight = totalRight + 1
            
        elif y >= 700 and y <=799 and solution is 7:
            right = right + 1
            totalRight = totalRight + 1
                        
        elif y >= 800 and y <=899 and solution is 8:
            right = right + 1
            totalRight = totalRight + 1
            
        elif y >= 900 and y <=999 and solution is 9:
            right = right + 1
            totalRight = totalRight + 1
            
        else:
            wrong = wrong + 1
            totalWrong = totalWrong + 1
        y = y + 1
        if y % 100 is 0:
            print("digit = " + str(int(y/100)-1) + ", right = " + str(right) + ", wrong = " + str(wrong))
            right = 0
            wrong = 0
    print("\nTotal:\tright = " + str(totalRight) + ", wrong = " + str(totalWrong) + ", " + str(round(float(totalRight/1000 * 100), 2)) + "%\n")
