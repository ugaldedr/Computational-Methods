"""
   Name: Dario Ugalde
   MavID: 1001268068
   Course: CSE 4345 Computational Methods
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img1 = mpimg.imread('book_fausett_gray.jpg')
img2 = mpimg.imread('book_horstmann1_gray2.png')
img3 = mpimg.imread('book_horstmann1_gray.jpg')

plt.figure(1)
plt.subplot(131)
plt.imshow(img1)

plt.subplot(132)
plt.imshow(img2)

plt.subplot(133)
plt.imshow(img3)

plt.show()

fro1 = np.linalg.norm(img1, 'fro')
fro2 = np.linalg.norm(img2, 'fro')
fro3 = np.linalg.norm(img3, 'fro')

one_two = fro1 - fro2
two_three = fro2 - fro3
one_three = fro1 - fro3

stack1 = np.column_stack(img1)
stack2 = np.column_stack(img2)
stack3 = np.column_stack(img3)

one_two_2 = np.linalg.norm(stack1) - np.linalg.norm(stack2)
two_three_2 = np.linalg.norm(stack2) - np.linalg.norm(stack3)
one_three_2 = np.linalg.norm(stack1) - np.linalg.norm(stack3)

print("book_fausett_gray.jpg, book_horstmann1_gray2.png")
print("   Frobenious norm = ",one_two)
print("   Second norm = ", one_two_2)
print("\nbook_horstmann1_gray2.png, book_horstmann1_gray.jpg")
print("   Frobenius norm = ",two_three)
print("   Second norm = ",two_three_2)
print("\nbook_fausett_gray.jpg, book_horstmann1_gray.jpg")
print("   Frobenius norm = ", one_three)
print("   Second norm = ", one_three_2)
