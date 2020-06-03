#Set Content
print('A set is a unique collection of objects in Python. You can denote a set \nwith a curly bracket {}. Python will automatically remove duplicate items:')


#create a set

set1={'khadak','ram','surakshya','amar','khadak'}
print(set1)


print('You can also create a set from a list as follows:')



#convert list to 

album_list = ["Michael jackson", "Thriller", 1986, "00:42:19",\
				"Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)
print(album_set)


print('Now let us create a set of genres:')
#Convert list to set

music_genres = set(["pop","pop","rock", "folk rock", "hard rock", "soul",\
				"Progressive rock", "soft rock", "R&B", "disco"])
print(music_genres)


#Set Operations
print('Let us go over set operations, as these can be used to change \nthe set. Consider the set A:')
#Sample set

A = set(["Thriller", "Back in Black","AC/DC"])
print(A)


print('We can add an element to a set using the add() method:')
A.add("NSYNC")
print(A)


print('If we add the same element twice, nothing will happen \nas there can be no duplicates in a set:')
A.add("NSYNC")
print(A)

print('We can remove an item from a set using the remove method:')
A.remove("NSYNC")
print(A)


print('We can verify if an element is in the set using the in command:')
"AC/DC" in A


#Sets Logic Operations

print('Remember that with sets you can check the\n difference between sets as well as the symmetric difference, intersection, and union:')

#Consider the following two sets:

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
print(album_set1,album_set2)


print('As both sets contain AC/DC and Back in Black we represent \nthese common elements with the intersection of two circles.')
print('You can find the intersect of two sets as follow using &:')
intersection = album_set1 & album_set2
print(intersection)


print('You can find all the elements that are only \ncontained in album_set1 using the difference method:')
difference1 = album_set1.difference(album_set2)
difference2 = album_set2.difference(album_set1)
print(difference1)
print(difference2)



print('The union is given by:')
union = album_set1.union(album_set2)
print(union)


print('And you can check if a set is a superset or subset\n of another set, respectively, like this')
#Check if superset
superset1 = set(album_set1).issuperset(album_set2)
superset2 = set(album_set2).issuperset(album_set1)
print(superset1)
print(superset2)




output
................
A set is a unique collection of objects in Python. You can denote a set
with a curly bracket {}. Python will automatically remove duplicate items:
{'amar', 'khadak', 'surakshya', 'ram'}
You can also create a set from a list as follows:
{65, 1986, 'Michael jackson', '00:42:19', 'Thriller', 'Pop, Rock, R&B', 10.0, 46.0, None, '30-Nov-82'}
Now let us create a set of genres:
{'hard rock', 'rock', 'folk rock', 'soft rock', 'soul', 'Progressive rock', 'R&B', 'disco', 'pop'}
Let us go over set operations, as these can be used to change
the set. Consider the set A:
{'Thriller', 'Back in Black', 'AC/DC'}
We can add an element to a set using the add() method:
{'Thriller', 'Back in Black', 'AC/DC', 'NSYNC'}
If we add the same element twice, nothing will happen
as there can be no duplicates in a set:
{'Thriller', 'Back in Black', 'AC/DC', 'NSYNC'}
We can remove an item from a set using the remove method:
{'Thriller', 'Back in Black', 'AC/DC'}
We can verify if an element is in the set using the in command:
Remember that with sets you can check the
 difference between sets as well as the symmetric difference, intersection, and union:
{'Thriller', 'AC/DC', 'Back in Black'} {'AC/DC', 'The Dark Side of the Moon', 'Back in Black'}
As both sets contain AC/DC and Back in Black we represent
these common elements with the intersection of two circles.
You can find the intersect of two sets as follow using &:
{'AC/DC', 'Back in Black'}
You can find all the elements that are only
contained in album_set1 using the difference method:
{'Thriller'}
{'The Dark Side of the Moon'}
The union is given by:
{'Thriller', 'AC/DC', 'The Dark Side of the Moon', 'Back in Black'}
And you can check if a set is a superset or subset
 of another set, respectively, like this
False
False
