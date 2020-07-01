myString  = "This String is not a Number"
try:
	print("Converting myString to int")
	print(1/0)
	print("String # " + 1 + ": "+ myString)
	myInt = int(myString)
	print(myInt)
except (ValueError, TypeError) as error:
	print("A ValueError or TypeError occureed.")
except Exception as error:
	print("Some other type of error occurred.")
	
print("Done!")
