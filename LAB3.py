print('When we set one variable B equal to A;\n both A and B are referencing the same list in memory:')
# Copy (copy by reference) the list A
A =["Khadak Bogati",10,1.2]
B = A
print('A:',A)
print('B:',B) 


print('Initially, the value of the first element in B is set as hard rock. If we change the\n first element in A to banana, we get an unexpected side effect. As A and B are\n referencing the same list, if we change list A, then list B also changes. \nIf we check the first element of B we get banana instead of hard rock:')
print('B[0]:', B[0])
A[0] = 'banana'
print('B[0]:',B[0])

print('You can clone list A by using the following syntax:')
B = A[:]
print(B)


print('Now if you change A, B will not change:')
print('B[0]:', B[0])
A[0] = "hard rock"
print('B[0]:', B[0])


# question 1
a_list = [1, 'hello', [1, 2, 3] , True]
print(a_list)
print(a_list[1])


print('Retrieve the elements stored at index 1, 2 and 3 of a_list.')

print(a_list[1:4])


print("Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:")

x = [1, 'a'] 
y = [2, 1, 'd']
print(x + y)





output
...............
When we set one variable B equal to A;
 both A and B are referencing the same list in memory:
A: ['Khadak Bogati', 10, 1.2]
B: ['Khadak Bogati', 10, 1.2]
Initially, the value of the first element in B is set as hard rock. If we change the
 first element in A to banana, we get an unexpected side effect. As A and B are
 referencing the same list, if we change list A, then list B also changes.
If we check the first element of B we get banana instead of hard rock:
B[0]: Khadak Bogati
B[0]: banana
You can clone list A by using the following syntax:
['banana', 10, 1.2]
Now if you change A, B will not change:
B[0]: banana
B[0]: banana
[1, 'hello', [1, 2, 3], True]
hello
Retrieve the elements stored at index 1, 2 and 3 of a_list.
['hello', [1, 2, 3], True]
Concatenate the following lists A = [1, 'a'] and B = [2, 1, 'd']:
[1, 'a', 2, 1, 'd']
