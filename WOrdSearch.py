 def front_times(str, n):
	front_len = 3
	if front_len > len(str):
		front_len = len(str)
	front = str[:front_len]

	result = ""
	for i in range(n):
		result = result + front
	return result

print(front_times('Chocolate', 3))













========================================================================================================
'''
GIven a string and a non-nagative int n, we'll say that the front of the string
is the first 3 chars, or whatever is there if the string is less than lenght3. return n copeis of front;
'''
def front_times(str, n):
	front_len = 3
	if front_len > len(str):
		front_len = len(str)
	front = str[:front_len]

	result = ""
	for i in range(n):
		result = result+front 
	return result

print(front_times('Khadak',2))
