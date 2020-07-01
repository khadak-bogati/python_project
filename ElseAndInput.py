try:
	inputFile = open("inputFile.txt", mode = "r")
except IOError as error:
	print("An input error occurred")
else:
	for line in inputFile:
		print(line)
	inputFile.close()
