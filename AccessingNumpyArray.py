import numpy as np 
import matplotlib.pyplot as plt 

print("Create a 2D Numpy Array")
print("Consider the list a, the list contains three nested list each of equal size")
a = [[11, 12, 13],[21, 22, 23],[31, 32, 33]]
print(a)
print()
print("We can cast the list to a Numpy array as follow")
print("convert list to numpy array , every element is the same type")
A= np.array(a)
print(A)


print()
print("========================================================================")
print("We can use the attribute ndim to obtain the number of axes or dimensions refereed to as the rank")
print("Show the numpy array dimensions")
print(A.ndim)

print()
print("===============================================================================")
print("Attribute shape return a tuple corresponding to the size or number of each dimension")
print("Show the numpy array shape")
print(A.shape)
print()
print("========================================================================")
print("The total number of element in the array is given by the attribute size")
print("Show the numpy array size")
print(A.size)


print()
print()
print("====================================================================")
print("Accessing different elements of a Numpy Array")
print("We Simply use the square bracket and indices correspoinding to the elements we would like: ")
print()
print("=======================================================================")
print("Acess the elements on the second row and third colume: ")
print(A[1, 2])
print()
print("Acess the elementson the first row and third colume: ")
print(A[0, 2])
print()
print("Acess the elements the third row and second colume: ")
print(A[2, 1])

print("==================================================================")
print()
print("we can also use the following notation to obtain the elements: ")
print(" Acess the elements on the second row and third cloume: ")
print(A[1][2])
print()
print("We can also use the following notion to obtain the elements")
print("We can Acess the elements as following")
print("Acess the elements on the first row and first cloume")
print()
print(A[0][0])
print("==========================================================================")
print("Acess the elements on the first row and first and second colume: ")
print(A[0][0:2])
print()
print("===========================================================================")
print()
print("Access the elements on the first and second row and third colume: ")
print(A[1:3, 2])



output
...........................................
Create a 2D Numpy Array
Consider the list a, the list contains three nested list each of equal size
[[11, 12, 13], [21, 22, 23], [31, 32, 33]]

We can cast the list to a Numpy array as follow
convert list to numpy array , every element is the same type
[[11 12 13]
 [21 22 23]
 [31 32 33]]

========================================================================
We can use the attribute ndim to obtain the number of axes or dimensions refereed to as the rank
Show the numpy array dimensions
2

===============================================================================
Attribute shape return a tuple corresponding to the size or number of each dimension
Show the numpy array shape
(3, 3)

========================================================================
The total number of element in the array is given by the attribute size
Show the numpy array size
9


====================================================================
Accessing different elements of a Numpy Array
We Simply use the square bracket and indices correspoinding to the elements we would like:

=======================================================================
Acess the elements on the second row and third colume:
23

Acess the elementson the first row and third colume:
13

Acess the elements the third row and second colume:
32
==================================================================

we can also use the following notation to obtain the elements:
 Acess the elements on the second row and third cloume:
23

We can also use the following notion to obtain the elements
We can Acess the elements as following
Acess the elements on the first row and first cloume

11
==========================================================================
Acess the elements on the first row and first and second colume:
[11 12]

===========================================================================

Access the elements on the first and second row and third colume:
[23 33]
