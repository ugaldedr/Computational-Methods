"""
    Name:   Dario Ugalde
    MavID:  1001268068
    Course: CSE 4345 Computational Methods
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def resizeImage(name) :
    book = mpimg.imread(name)
    resize = np.ones((2 * len(book) - 1, 2 * len(book[0]) - 1, len(book[0,0])))
    for i in range(0,len(resize[0,0])):
        for x in range(0,len(resize)):
            for y in range(0,len(resize[0])-2):
                if x % 2 is 0:
                    x1 = book[int((x+1)//2),int((y+1)//2),i]
                    x2 = book[int((x+1)//2),int(((y+1)//2)+1),i]
                    if y % 2 is 0:
                        resize[x,y,i] = np.uint8(x1)
                    elif y % 2 is 1:
                        resize[x,y,i] = np.uint8(x1//2 + x2//2)
                        resize[x,y+1,i] = np.uint8(x1)
                elif x % 2 is 1:
                    x1 = book[int(((x+1)//2)-1),int((y+1)//2),i]
                    x2 = book[int((x+1)//2),int((y+1)//2),i]
                    x3 = book[int((x+1)//2),int(((y+1)//2)+1),i]
                    x4 = book[int(((x+1)//2)-1),int(((y+1)//2)+1),i]
                    if y % 2 is 0:
                        resize[x,y,i] = np.uint8(x1//2+x2//2)
                    elif y % 2 is 1:
                        resize[x,y,i] = np.uint8(x1//4+x2//4+x3//4+x4//4)
                        resize[x+1,y,i] = np.uint8(x3//2+x4//2)
    merge = mpimg.imsave("output.jpg",resize)
    merge = mpimg.imread("output.jpg")
    plt.figure()
    plt.subplot(121)
    plt.title("Original Image")
    plt.imshow(book)
    plt.subplot(122)
    plt.title("Interpolated Image")
    plt.imshow(merge)
    
    plt.show()

####################  main  ####################
if __name__ == "__main__" :
    filename = "book_fausett_small.jpg"
    resizeImage(filename) 
