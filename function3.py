ex=================1

print("The return() function is particularly useful if you have any IF statements in the function,\n when you want your output to be dependent on some condition:")
print()
print("Function Example")
def type_of_album(artist, album, year_released):
	print(artist, album, year_released)
	if year_released > 1980:
		return "Mordern"
	else:
		return "Oldie"
x = type_of_album("Michael Jackson", "Thriller", 1980)
print(x)

output
..................
The return() function is particularly useful if you have any IF statements in the function,
 when you want your output to be dependent on some condition:

Function Example
Michael Jackson Thriller 1980
Oldie


ex============================2

print("We can use a loop in a function. For example, we can print out each element in a list:")
print()
print("Function Example")
def printlist(the_list):
	for element in the_list:
		print(element)
print("===========================================")
printlist(['2', 1, 'the man', 'abc'])

output
Function Example
===========================================
2
1
the man
abc



ex===================================================3
print("===============================")
print("You can set a default value for arguments in your function.")
print()

def isGoodRating(rating =4):
	if(rating < 7):
		print("This album sucks its rating is", rating)
	else:
		print("This album is good its rating is", rating)
isGoodRating()
isGoodRating(10)
isGoodRating(6)


output
===============================
You can set a default value for arguments in your function.

This album sucks its rating is 4
This album is good its rating is 10
This album sucks its rating is 6

ex----------------5
print("Example of global variable")
artist = "Michael Jackson"
def printer1(artist):
	internal_var = artist
	print(artist, 'is an artist')
printer1(artist)

output
Example of global variable
Michael Jackson is an artist


ex=================================6
print("===================================================")
print("But there is a way to create global variables from within a function as follows:")
artist= 'Michael Jackson'
def printer(artist):
	global internal_var
	internal_var= "Whitney Houston"
	print(artist, 'is an artist')
printer(artist)
printer(internal_var)

output
===================================================
But there is a way to create global variables from within a function as follows:
Michael Jackson is an artist
Whitney Houston is an artist


