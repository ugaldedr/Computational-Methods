"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 4345 Computational Methods
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def intermediate(firstImage, lastImage, N, display) :
    """
        if display is True
            display the images
        otherwise
            save as a file with the names mid01.jpg, mid02.jpg, ...
    """

    young = mpimg.imread(firstImage)
    old = mpimg.imread(lastImage)
    count = 1
    stepTable = calculateStep(young,old,N)
    while count < N:
        mid = young + np.uint8(count * stepTable)
        if display:
            plt.figure()
            plt.title("Image {0:d}".format(count + 1))
            img = Image.fromarray(mid,'RGB')
            plt.imshow(mid)
            plt.show()
        else:
            plt.imsave("Image{0:d}.png".format(count+1),mid)
        count = count + 1

def calculateStep(img1, img2, N):
    stepTable = np.zeros((len(img1),len(img1[0]),len(img1[0,0])))
    for i in range(0,len(img1[0,0])):
        for x in range(0,len(img1)):
            for y in range(0,len(img1[0])):
                stepTable[x,y,i] = img2[x,y,i]/N - img1[x,y,i]/N
    return stepTable


###############  main  ###############
if __name__ == "__main__" :
    name1 = "darinYoung.jpg"  # first image
    name2 = "darinOld.jpg"    #  last image
    
    N = 10    # should produce N-1 intermediate images
    
    display = True   # True means display intermediate images
                     # False means save intermediate images
    intermediate(name1, name2, N, display)

