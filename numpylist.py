#import numpy
import numpy as np 
print("Create a numpy array")
print("==========================================")
a = np.array([0,1,2,3,4])
print("==========================================")

print("print each element ")
print("a[0]: ", a[0])
print("a[1]: ", a[1])
print("a[2]: ", a[2])
print("a[3]: ", a[3])
print("a[4]: ", a[4])

print("Check the type of the array")
print(type(a))
print(a.dtype)
print("=====================================================")
print("Create a numpy array")
b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print("Check the type of the array")
print(type(b))


# Assign Value
print("We can change the value of the array, consider the array c:")
c = np.array([20, 1, 2, 3, 4])
print(c)
print("========================================================")
print("We can change the first element of the array to 100 as follows: ")
c[0] = 100
print(c)

print(" Assign the 5 th  element to 0")
c[4] = 0
print(c)


print("==================================================================")
print()
print("Like list, we can not slice the numpy array, and we can selet the elemets\n from 10 to three and assign it to a new myphy array d as follows:")

d = c[1:4]
print(d)

print("===========================================")
print("we can assign the correspoinding index to new values as follows: ")
c[3:5] = 300, 400
print(c)
# asign value with list
print("Similary, we can use a list to select a specific index. The list select contains several values:")
print("===================================================================================")
print("create the index list")
select = [0, 2, 3]
print(" we can use the list as an argument in the brackets. the ouput is the element corresponding to the particular index:")
d = c[select]
print(d)



output

.................................................................................................

Create a numpy array
==========================================
==========================================
print each element
a[0]:  0
a[1]:  1
a[2]:  2
a[3]:  3
a[4]:  4
Check the type of the array
<class 'numpy.ndarray'>
int32
=====================================================
Create a numpy array
Check the type of the array
<class 'numpy.ndarray'>
We can change the value of the array, consider the array c:
[20  1  2  3  4]
========================================================
We can change the first element of the array to 100 as follows:
[100   1   2   3   4]
 Assign the 5 th  element to 0
[100   1   2   3   0]
==================================================================

Like list, we can not slice the numpy array, and we can selet the elemets
 from 10 to three and assign it to a new myphy array d as follows:
[1 2 3]
===========================================
we can assign the correspoinding index to new values as follows:
[100   1   2 300 400]
Similary, we can use a list to select a specific index. The list select contains several values:
===================================================================================
create the index list
 we can use the list as an argument in the brackets. the ouput is the element corresponding to the particular index:
[100   2 300]
