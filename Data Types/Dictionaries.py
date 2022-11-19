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