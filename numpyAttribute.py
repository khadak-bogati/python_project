#import numpy
import numpy as np 

print("==========================================================")
print("Create a numpy array")

a = np.array([0, 1, 2, 3, 4])
print(a)

print("==============================================================")
print("The attribute size is the number of element in the array: ")
print(a.size)

print("==============================================================")
print(" Get the number of dimensions of numpy array")
print(a.ndim)
print(a.shape)

print()
print("========================================================")
print("Create a numpy array")
a = np.array([1, -1, 1, -1])
print("Get the mean of numpy array")
mean = a.mean()
print(mean)

print("=====================================================")
print()
print("Get the standard deviation of numpy array")
standard_deviation=a.std()
print(standard_deviation)

print()
print("===================================================")
print("create a numpy array")
b = np.array([-1, 2, 3, 4, 5])
print(b)


print()
print("======================================================")
print("Get the biggest value in the numpy array")
max_b = b.max()
print(max_b)
print("get the smallest number in the numpy array")
min_b = b.min()
print(min_b)


output
================================================

==========================================================
Create a numpy array
[0 1 2 3 4]
==============================================================
The attribute size is the number of element in the array:
5
==============================================================
 Get the number of dimensions of numpy array
1
(5,)

========================================================
Create a numpy array
Get the mean of numpy array
0.0
=====================================================

Get the standard deviation of numpy array
1.0

===================================================
create a numpy array
[-1  2  3  4  5]

======================================================
Get the biggest value in the numpy array
5

C:\Users\khada\Desktop\Devops\Python>py project.py
==========================================================
Create a numpy array
[0 1 2 3 4]
==============================================================
The attribute size is the number of element in the array:
5
==============================================================
 Get the number of dimensions of numpy array
1
(5,)

========================================================
Create a numpy array
Get the mean of numpy array
0.0
=====================================================

Get the standard deviation of numpy array
1.0

===================================================
create a numpy array
[-1  2  3  4  5]

======================================================
Get the biggest value in the numpy array
5
get the smallest number in the numpy array
