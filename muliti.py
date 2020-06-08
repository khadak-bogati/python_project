#import numpy
import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt

# Plotting functions

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
# Plotting functions

def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)


print("==========================================================")
print("numpy Array Operations")
print("Array addition")
print()
print("Array Multiplication")
print("Create a numpy array")
print()

y= np.array([1, 2])
print(y)

print()
print("We can multiply every element in the array by 2: ")
z = 2 * y
print(z)

print()
print("=======================================================")
print("Product of two Numpy Array")
print("Consider the following array u: ")
print("create a numpy array")
print()
u = np.array([1, 2])
print(u)
print("Create a numpy array")
v = np.array([3, 2])
print(v)
print("The product of the two numpy array u and v is given by: ")
print(" Calculate the production of two numpy array: ")
z = u * v
print(z)

print()
print("dot product")
print("The dot product of the two numpy array u and v is given by: ")
print(" Calculate the dot product")
print()

print(np.dot(u,v))

print()
print("Adding the constant 1 to each elementin the array")
print(" Add the constant to array")
print(u + 1)

print()
print(" Mathematical functions")
print(" We can access the value of pie in numpy as follows: ")
print(np.pi)
print()
print("We can create the following numpy array in Radians: ")
print("Create the numpy array in radians: ")
x = np.array([0, np.pi/2, np.pi])
print(x)

print()
print("we can apply the functions sin to the array x and assign the values to the array y")
print("Calculate the sin of each elements: ")
y = np.sin(x)
print(y)


Output
....................

==========================================================
numpy Array Operations
Array addition

Array Multiplication
Create a numpy array

[1 2]

We can multiply every element in the array by 2:
[2 4]

=======================================================
Product of two Numpy Array
Consider the following array u:
create a numpy array

[1 2]
Create a numpy array
[3 2]
The product of the two numpy array u and v is given by:
 Calculate the production of two numpy array:
[3 4]

dot product
The dot product of the two numpy array u and v is given by:
 Calculate the dot product

7

Adding the constant 1 to each elementin the array
 Add the constant to array
[2 3]

 Mathematical functions
 We can access the value of pie in numpy as follows:
3.141592653589793

We can create the following numpy array in Radians:
Create the numpy array in radians:
[0.         1.57079633 3.14159265]

we can apply the functions sin to the array x and assign the values to the array y
Calculate the sin of each elements:
[0.0000000e+00 1.0000000e+00 1.2246468e-16]
