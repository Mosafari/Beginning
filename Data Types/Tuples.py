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
print()  #empty line

# we can't add, remove, and update values of tuples just as we do on lists, but we can convert tuples to lists
# and modify it and then turn it into a tuple using tuple() constructor.

print(tup1)
temp = list(tup1)
temp.pop()
tup1= tuple(temp)
print(tup1)
print()  #empty line

# Unpack Tuples

#  Unpacking a Tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

packing = (1,2,"value")
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
(num1,num2,string) = packing
print(num1,'\n',num2,'\n',string)
print()  #empty line
# Note: The number of variables must match the number of values in the tuple, if not,
# you must use an asterisk to collect the remaining values as a list.

# Using Asterisk*
# If the number of variables is less than the number of values,
# you can add an * to the variable name and the values will be assigned to the variable as a list:

pack2 = (1,2,3,4,5,'str1','str2')
(*numbers,string1,string2) = pack2
print(numbers,'\n',string1,'\n',string2)
print() #empty line

#                                      *** ( loop in Tuple )  in loop section ***

# Join Tuples

#  Join Two Tuples
# To join two or more tuples you can use the + operator:

P = pack2 + packing
print(P)
print() #empty line

#  Multiply Tuples
# If you want to multiply the content of a tuple a given number of times, you can use the * operator:

P2 = pack2 * 2
print(P2)
print() #empty line

# more tuple methods on : https://www.w3schools.com/python/python_tuples_methods.asp