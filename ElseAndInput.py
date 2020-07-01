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
