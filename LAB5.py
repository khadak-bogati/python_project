print("Let's assign a a value of 5. Use the equality operator denoted with two equal == signs to determine if two values \nare equal. The case below compares the variable a with 6.")
a = 5
print(a == 6)
print(a)


print('Set i = 2. The statement is false as 2 is not greater than 5:')

#Greater than Sign
i = 2
print(i > 2)


print('The inequality test uses an exclamation mark preceding the equal sign, if two operands are\n not equal then the condition becomes True. For example, the following \ncondition will produce True as long as the value of i is not equal to 6:')
#Ienquality Sign

print(i != 6)


print('When i equals 6 the inequality expression produces False.')
i = 6
print(i != 6)


print('We can apply the same methods on strings. For example, use an equality operator on two different \nstrings. As the strings are not equal, we get a False.')
#Use Equality sign to compare the string

print("ACDC" == "khadak")

print('If we use the inequality operator, the output is going to be True as the strings are not equal.')
#use inequality sing to compare the string
print("ACDC" != "khadak")

#Inequality operation is also used to compare the letters/words/symbols according to the ASCII value of letters. The decimal value shown in the following table represents the order of the character:

#For example, the ASCII code for ! is 21, while the ASCII code for + is 43. Therefore + is larger than ! as 43 is greater than 21.

#Similarly, the value for A is 101, and the value for B is 102 therefore:

print('Compare characters')
print('B'> 'A')
print('B' > 'a')


print('When there are multiple letters, the first letter takes precedence in ordering:')
print('BA' > 'AB')



output
...........................
Let's assign a a value of 5. Use the equality operator denoted with two equal == signs to determine if two values
are equal. The case below compares the variable a with 6.
False
5
Set i = 2. The statement is false as 2 is not greater than 5:
False
The inequality test uses an exclamation mark preceding the equal sign, if two operands are
 not equal then the condition becomes True. For example, the following
condition will produce True as long as the value of i is not equal to 6:
True
When i equals 6 the inequality expression produces False.
False
We can apply the same methods on strings. For example, use an equality operator on two different
strings. As the strings are not equal, we get a False.
False
If we use the inequality operator, the output is going to be True as the strings are not equal.
True
Compare characters
True
False
When there are multiple letters, the first letter takes precedence in ordering:
True
