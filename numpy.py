import time
import sys
import numpy as numpy

import matplotlib.pyplot as plt 

#plotting functions
def Plotvec1(u, z, v):

	ax = plt.axes()
	ax.arrow(0, 0, *u, head_width=0.05, color ='r', head_length=0.1)
	plt.text(*(u + 0.1), 'u')

	ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
	plt.text(*(v + 0.1), 'v')
	ax.arrow(0, 0, *z , head_width=0.05, head_length=.01)
	plt.text(*(z + 0.1), 'z')
	plt.ylim(-2, 2)
	plt.xlim(-2, 2)

	def Plotvec2(a, b):
		ax = plt.axes()
		ax.arrow(0, 0, *a, head_width=0.05, color='r', head_length=0.1)
		plt.text(*(a + 0.1), 'a')
		ax.arrow(0, 0, *b, head_width=0.05, color = 'b', head_length=0.01)
		plt.text(*(b + 0.1), 'b')
		plt.ylim(-2, 2)
		plt.xlim(-2, 2)
# Create a python list
a = ["0", 1, "two", "3", 4]

#print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

#Check the type of the array
print(type(a))




output
.......................
a[0]: 0
a[1]: 1
a[2]: two
a[3]: 3
a[4]: 4
<class 'list'>
