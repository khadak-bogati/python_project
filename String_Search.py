''''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
'''
def string_search(str):
	result = ""
	for i in range(len(str)):
		if i % 2 ==0:
			result = result + str[i]
	return result
print(string_search('Kkhhaaddaakk'))