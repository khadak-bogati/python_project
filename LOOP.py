r = ['khadak', 'bogati', 'amar', 'ram']
l=len(r)
print("...............................")
print('there is length of r is ',l)
print("...............................")
for i in range(l):
	print("The range of r is :",i)
  
  
  output
  
  ...............................
there is length of r is  4
...............................
The range of r is : 0
The range of r is : 1
The range of r is : 2
The range of r is : 3


#####
print("================================================================")
print("In this example we can print out a sequence of numbers from 0 to 7:")
print("================================================================")

for i in range(0,8):
	print(i)
print("================================================================")

output
================================================================
In this example we can print out a sequence of numbers from 0 to 7:
================================================================
0
1
2
3
4
5
6
7
================================================================



Ex========3

print("============================================")
print("In Python we can directly access the elements in the list as follows:")
#Example of for loop, loop thought list
dates = [1982,1986,1989]
for year in dates:
	print(year)


output
===================================================================
In Python we can directly access the elements in the list as follows:
1982
1986
1989


ex==========4
print("==============================")
print("We can change the elements in a list:")
print("=======================================")

colores = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0,5):
	print('Before colores', i, 'is', colores[i])
	colores[i] = 'black'
	print('After colores',i, 'is', colores[i])
  
  output
  We can change the elements in a list:
=======================================
Before colores 0 is red
After colores 0 is black
Before colores 1 is yellow
After colores 1 is black
Before colores 2 is green
After colores 2 is black
Before colores 3 is purple
After colores 3 is black


ex====================5
print("==============================")
print("We can access the index and the elements of a list as follows:")
print("=======================================")

colores = ['red', 'yellow', 'green', 'purple', 'blue']

for i, color in enumerate(colores):
	print(i,'\t',color)


output
==============================
We can access the index and the elements of a list as follows:
=======================================
0        red
1        yellow
2        green
3        purple
4        blue


ex====================6

