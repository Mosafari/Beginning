# Tuples
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data,
# the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

tup1 = (1,2,2,3,'a','b')

#  Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

# Tuple Length

print(len(tup1)) # output : 6
print()  #empty line

#  Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

tup = (1,)
print(type(tup))
print()  #empty line

# *Set items are unchangeable, but you can remove and/or add items whenever you like.
# **As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

# When choosing a collection type, it is useful to understand the properties of that type.
# Choosing the right type for a particular data set could mean retention of meaning, and,
# it could mean an increase in efficiency or security.


tup2= (9,8,7)
tup1+=tup2
print(tup1)
print(tup1[2:5])
print(tup2[2])

# we can't add, remove, and update values of tuples just as we do on lists, but we can convert tuples to lists
# and modify it and then turn it into a tuple using tuple() constructor.

print(tup1)
temp = list(tup1)
temp.pop()
tup1= tuple(temp)
print(tup1)