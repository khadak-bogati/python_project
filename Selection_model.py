def Selection_model(a_list):
	for i in range(len(a_list)):
		minIndex = i
		for j in range(i + 1, len(a_list)):
			if a_list[minIndex] > a_list[j]:
				minIndex = j
		minValue = a_list[minIndex]
		del a_list[minIndex]
		a_list.insert(i, minValue)
	return a_list
print(Selection_model([6, 5, 4, 3, 2, 1]))
