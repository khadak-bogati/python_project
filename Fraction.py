class Fraction:
	def __init__(self, top, bottom):
		self.num = top
		self.den = bottom
	def __str__(self):
		return str(self.num) + "/" + str(self.den)
	def getNum(self):
		return self.num
	def getDen(self):
		return self.den
myFraction = Fraction(8, 9)
print(myFraction)
print(myFraction.getNum())
print(myFraction.getDen())
