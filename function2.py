print("Functions make Things Simple")
#Block
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * b1 -1
if(c1 < 0):
	c1 = 0
else:
	c1 = 5
print(c1)


output
.............
5


ex===============2
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2   


output
=============
0

print("===========================================")
print("Pre-definded functions")
print()

album_ratings = [10.0,20,8.5,9.5,7.5,6.6,9.0,4.5]
print(album_ratings)

print("The sum() function adds all the elements in a list or tuple:")
print(sum(album_ratings))

print()
print("The len() function returns the length of a list or tuple:")
print("========================================")
print(len(album_ratings))


output
===========================================
Pre-definded functions

[10.0, 20, 8.5, 9.5, 7.5, 6.6, 9.0, 4.5]
The sum() function adds all the elements in a list or tuple:
75.6

The len() function returns the length of a list or tuple:
========================================
8


