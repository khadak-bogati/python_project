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
print(" Considet the numpy array U: ")

u = np.array([1, 0])
print(u)

print("Consider the numpy array V: ")
v = np.array([0, 1])
print(v)

print()
print("=========================================================")
print("We can add the two arrays and assign it to z ")
print("numpy array Addition")

z= u + v
print(z)

print()
print("==============================================================")
print(" The Operations is equivalent to vector addition: ")
print("Plot numpy array")

print(Plotvec1(u, z, v))


output
..............................
==========================================================
numpy Array Operations
Array addition

 Considet the numpy array U:
[1 0]
Consider the numpy array V:
[0 1]

=========================================================
We can add the two arrays and assign it to z
numpy array Addition
[1 1]

==============================================================
 The Operations is equivalent to vector addition:
Plot numpy array

C:\Users\khada\Desktop\Devops\Python>py project.py
==========================================================
numpy Array Operations
Array addition

 Considet the numpy array U:
[1 0]
Consider the numpy array V:
[0 1]

=========================================================
We can add the two arrays and assign it to z
numpy array Addition
[1 1]

==============================================================
 The Operations is equivalent to vector addition:
Plot numpy array
None
