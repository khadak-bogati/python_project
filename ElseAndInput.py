try:
	inputFile = open("inputFile.txt", mode = "r")
except IOError as error:
	print("An input error occurred")
else:
	for line in inputFile:
		print(line)
	inputFile.close()

	
	.......................................................
	
	
inputFile = open("NumberFile.txt", mode = "r")
try:
	for line in inputFile:
		print(int(line))
except ValueError as error:
	print("A value error occureed!")
else:
	print("No errors occureed! ")
finally:
	inputFile.close()

	
	
	...................................................................................
try:
	inputFile = open("NumberFile.txt", mode = "r")
	try:
		for line in inputFile:
			print(int(line))
	except ValueError as error:
		print("A value error occurred!")
	else:
		print("No errors occurred converting the file! ")
	finally:
		inputFile.close()
except IOError as error:
	print("An error occurred reading the file!")
