L= ["Michael Jackson",10.1,1982]
print(L)
print('The same element using nagative and positive indexing:\n positive: ',L[0],
	'\n Negative: ',L[-3])
print('The same element using nagative and positive indexing:\n positive: ',L[1],
	'\n Negative: ',L[-2])
print('The same element using nagative and positive indexing:\n positive: ',L[2],
	'\n Negative: ',L[-1])



print('This is seprerate example of listing slicing')
L2=["Michael Jackson",10.1,1982,"MJ",1]
print(L2)
print(L2[3:5])

print('We can use the method extend to add new elements to the list:')
L3=["Michael Jackson",10.1,1982]
L3.extend(['pop',10])
print(L3)

print('Another similar method is append. If we apply append instead of extend, we add one element to the list:')
L4=["Michael Jackson",10.1,1982]
L4.append(['Khadak',20])
print(L4)


print("If we append the list ['a','b'] we have one new element consisting of a nested list:")
L5=["Michael Jackson",10.1,1982]
L5.append(['a','b'])
print(L5)



print('As lists are mutable, we can change them. For example, we can change the first element as follows:')
A=["disco",10,10.2]
print('Before change: ',A)
A[0]='hard rock'
print('After Change: ',A)

print('We can convert a string to a list using split. For example, the method split translates every group of \ncharacters separated by a space into an element in a list:')
# Split the string, default is by space
L6='hard rock'
print(L6.split())



print('We can use the split function to separate strings on a specific character.\n We pass the character we would like to split on into the argument,\n which in this case is a comma. The result is a list, and each element corresponds\n to a set of characters that have been separated by a comma:')
L8='A,B,C,D,E'
print(L8.split(','))







OUT PUT
..............
['Michael Jackson', 10.1, 1982]
The same element using nagative and positive indexing:
 positive:  Michael Jackson
 Negative:  Michael Jackson
The same element using nagative and positive indexing:
 positive:  10.1
 Negative:  10.1
The same element using nagative and positive indexing:
 positive:  1982
 Negative:  1982
This is seprerate example of listing slicing
['Michael Jackson', 10.1, 1982, 'MJ', 1]
['MJ', 1]
We can use the method extend to add new elements to the list:
['Michael Jackson', 10.1, 1982, 'pop', 10]
Another similar method is append. If we apply append instead of extend, we add one element to the list:
['Michael Jackson', 10.1, 1982, ['Khadak', 20]]
If we append the list ['a','b'] we have one new element consisting of a nested list:
['Michael Jackson', 10.1, 1982, ['a', 'b']]
As lists are mutable, we can change them. For example, we can change the first element as follows:
Before change:  ['disco', 10, 10.2]
After Change:  ['hard rock', 10, 10.2]
We can convert a string to a list using split. For example, the method split translates every group of
characters separated by a space into an element in a list:
['hard', 'rock']
We can use the split function to separate strings on a specific character.
 We pass the character we would like to split on into the argument,
 which in this case is a comma. The result is a list, and each element corresponds
 to a set of characters that have been separated by a comma:
['A', 'B', 'C', 'D', 'E']
