#  Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
list1=[1,2,2,2,3]
set0 = set(list1)
print(set0)
set1 ={1,2,3,3,3,True,'str','str'}
print(set1)
print(len(set1))
print(type(set1))
print() #empty line