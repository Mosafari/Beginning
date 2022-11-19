#  Set
# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.

# The set() Constructor
# It is also possible to use the set() constructor to make a set.
list1=[1,2,2,2,3,'python','test']
set0 = set(list1)
print(set0)
set1 ={1,2,3,3,3,True,'str','str'}
print(set1)
print(len(set1))
print(type(set1))
print() #empty line

#  Add Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.

set1.add(22)
print(set1)
print() #empty line

#  Add Sets
# To add items from another set into the current set, use the update() method.

set1.update(set0)
print(set1)
print() #empty line

#  Add Any Iterable
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).

list2 =[4,5,6,6,6,6,7]
set1.update(list2)
print(set1)
print() #empty line

