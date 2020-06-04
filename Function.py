print("===========================================")
print('An example of a function that adds on to the parameter a prints and returns the output as b:')

def add(a):
	b = a + 1
	print(a, 'if you add one', b)
	return(b)
add(2)

........................
output
===========================================
An example of a function that adds on to the parameter a prints and returns the output as b:
2 if you add one 3



ex================2
print("======================================")
print("A variable that is declared outside a function definition is a global variable, and its value is accessible and modifiable throughout the program. We will discuss more about global variables at \nthe end of the lab.")
def square(a):
	b = 1
	c = a * a + b
	print(a, "if you square + 1", c)
	return(c)
print()
print("=======================================")
print("We can call the function with an input of ")
square(5)
x = 3
y = square(x)
print(y)

output

======================================
A variable that is declared outside a function definition is a global variable, and its value is accessible and modifiable throughout the program. We will discuss more about global variables at
the end of the lab.

=======================================
We can call the function with an input of
5 if you square + 1 26
3 if you square + 1 10
10




ex=====================================3
print("==============================================")
print("If there is no return statement, the function returns None.\n The following two functions are equivalent:")
print()

def MJ():
	print('Michael Jackson')

def MJ1():
	print('Michael Jackson')
	return(None)
MJ()

MJ1()


output
==============================================
If there is no return statement, the function returns None.
 The following two functions are equivalent:

Michael Jackson
Michael Jackson


ex==============================4
def Mult(a, b):
	c = a * b
	return(c)
print(Mult(5, 6))

output
.............
30

ex=====================================5

print("==========================================")
print("Function Definition")

def square(a):
	#Local variable b
	b = 1
	c = a * a + b
	print(a, "if you square + 1", c)
	return(c)
x=5
z=square(x)


==========================================
Function Definition
5 if you square + 1 26


ex===================================6

print("==========================================")
print("Function Definition")

def square(a):
	#Local variable b
	c = 1
	b = a * a + c
	print(a, "if you square + 1", b)
	return(b)
x=2
z=square(x)


output
==========================================
Function Definition
2 if you square + 1 5



