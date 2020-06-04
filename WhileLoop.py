ex=========================1
print("========================================================")
print("While loop example")
dates = ['jan', 'feb', 'march', 'april', 'may']

i = 0
months =0

while(months != 'april'):
	months = dates[i]
	i = i + 1
	print(months)
print('It took ', i , 'repetitions to get out of loop')

output
========================================================
While loop example
jan
feb
march
april
It took  4 repetitions to get out of loop



------------------------------
for i in range(-5,6):
	print(i)
  
  --------------------------------------
  -5
-4
-3
-2
-1
0
1
2
3
4
5


ex ==================================2
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rate = PlayListRatings[0]

while(rate >= 6):
	print(rate)
	rate = PlayListRatings[i]
	i = i + 1
	
print(" it took ", i, "repetitions to get out of loop")


output 
.............
10
10
9.5
10
8
7.5


# Write a while loop to copy the strings 'orange' of the list 
squares to the list new_squares. Stop and exit the loop if the value on the list is not 'orange':

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0
while(squares[i] == 'orange'):
	new_squares.append(squares[i])
	i = i + 1
print(new_squares)


out put
------------------------
['orange', 'orange']


ex ===============4
names = ['khadak', 'khadak', 'khadak', 'ram', 'hari']
myneme=[]
i = 0

while(names[i] == 'khadak'):
	myneme.append(names[i])
	i = i + 1
print(myneme)


output
========================
['khadak', 'khadak', 'khadak']


