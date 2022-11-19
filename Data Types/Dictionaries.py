# Dictionaries

# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

D = {'a': 1, 'b': 2, 'c': 3}

# Dictionary Items
# Dictionary items are ordered, changeable, and does not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Ordered or Unordered?
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.

# **Dictionaries cannot have two items with the same key**

print(len(D))
print(type(D))
print() #empty line

# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets

print(D['a'])
print() #empty line

# There is also a method called get() that will give you the same result:

print(D.get('a'))
print(D.get('h')) # h key doesn't exist
print() #empty line

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.

print(D.keys())
print() #empty line
# The list of the keys is a view of the dictionary,
# meaning that any changes done to the dictionary will be reflected in the keys list.

# Get Values
# The values() method will return a list of all the values in the dictionary.

print(D.values())
print() #empty line
# The list of the values is a view of the dictionary,
# meaning that any changes done to the dictionary will be reflected in the values list.

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.

print(D.items())
print() #empty line
# The returned list is a view of the items of the dictionary,
# meaning that any changes done to the dictionary will be reflected in the items list.

# Change Dictionary Items

# Change Values
# You can change the value of a specific item by referring to its key name:

print(D)
D['a'] = "newvalue"
print(D)
print() #empty line

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

D.update({'newkey': 'value'})
print(D)
print() #empty line

# Add Dictionary Items

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

D["hello"] = "world"
print(D)
print() #empty line

# Update Dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
# The argument must be a dictionary, or an iterable object with key:value pairs.

# Remove Dictionary Items

# The pop() method removes the item with the specified key name:

D.pop("newkey")
print(D)
print() #empty line

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

D.popitem()
print(D)
print() #empty line

# The del keyword removes the item with the specified key name:

del D['a']
print(D)
print() #empty line

# **The del keyword can also delete the dictionary completely**

# The clear() method empties the dictionary:

D.clear()
print(D)
print() #empty line

#                                      *** ( loop in Dict )  in loop section ***

# Copy Dictionaries

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

A={1:'a',2:'b'}
D = A.copy()
print(D)
print() #empty line

# Another way to make a copy is to use the built-in function dict()
C = dict(A)
print(C)
print() #empty line
