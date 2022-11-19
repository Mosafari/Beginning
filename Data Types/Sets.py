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

# Remove Set Items

#  Remove Item
# To remove an item in a set, use the remove(), or the discard() method.

set1.remove("python")
print(set1)
set1.discard("nothing")
print(set1)
print() #empty line
# Note: If the item to remove does not exist, remove() will raise an error
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.

set1.pop()
print(set1)
print() #empty line
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:
set0.clear()
print("set0 : ",set0)
print() #empty line

#                                      *** ( loop in Set )  in loop section ***

# Join Sets

#  Join Two Sets
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets,
# or the update() method that inserts all the items from one set into another:

# Note: Both union() and update() will exclude any duplicate items.

set3 = {4,4,9,8}
test = set1.union(set3)
print(test)
set1.update(set3)
print(set1)
print() #empty line

# Keep ONLY the Duplicates
# The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)
print() #empty line

# The intersection() method will return a new set, that only contains the items that are present in both sets.

h = {"apple", "banana", "cherry"}
w = {"google", "microsoft", "apple"}

z = h.intersection(w)
print(z) 
print() #empty line

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

i = {"apple", "banana", "cherry"}
j = {"google", "microsoft", "apple"}

i.symmetric_difference_update(j)
print(i) 
print() #empty line

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

t = {"apple", "banana", "cherry"}
u = {"google", "microsoft", "apple"}

m = t.symmetric_difference(u)
print(m)
print() #empty line

# more set methods on : https://www.w3schools.com/python/python_sets_methods.asp