def bubble_model(myList):
	swap_occurred = True
	while swap_occurred:
		swap_occurred = False
		for item in range(len(myList) - 1):
			if myList[item] > myList[item + 1]:
				temp = myList[item]
				myList[item] = myList[item + 1]
				myList[item + 1] = temp
				swap_occurred = True
	return myList
print(bubble_model([9, 6, 4, 3, 1]))
