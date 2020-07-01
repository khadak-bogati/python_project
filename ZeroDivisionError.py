try:
	dividend = int(input("Enter dividend: "))
	divisor = int(input("Enter divisor: "))
	quotient = dividend / divisor
	
except ZeroDivisionError:
	print("We can't divide by 0!")
except ValueError:
	print("Please only enter integers!")
else:
	print("The quotient is", quotient)
print("Done!")
