myString = "Next, dive into our Leadership Principles. We use our Leadership Principles\
 every day, whether we're discussing ideas for new projects or deciding on the best approach \
  to solving a problem. It is just one of the things that makes Amazon peculiar. All \
   candidates are evaluated based on our Leadership Principles. The best way to prepare for \
   your interview is to consider how you ve applied the Leadership Principles in your \
   previous professional experience."
myString=myString.replace(".", "")
myString=myString.replace(",", "")
myString=myString.replace("'", "")
myString=myString.lower()
mySplitSpring=myString.split()
print(mySplitSpring)

myDictionary = {}

for word in mySplitSpring:
	if word in myDictionary:
		myDictionary[word] += 1
	else:
		myDictionary[word] = 1
print(myDictionary)
