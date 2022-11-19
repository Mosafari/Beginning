#  List
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data,
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets

A = []

#  List Items :
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

B = [1,1,2,3,"a","b","c"]
#length list
print(len(B)) # output : 7
print()  #empty line

#  Access Items
# List items are indexed and you can access them by referring to the index number:

print(B[2]) # output : 2
print()  #empty line

#  Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

print(B[-1]) # output : "c"
print()  #empty line

#  Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.

print(B[2:6]) # output : [2,3,"a","b"]
# Note: The search will start at index 2 (included) and end at index 5 (not included).
print()  #empty line

# Range of Negative Indexes
# Specify negative indexes if you want to start the search from the end of the list:

print(B[-5:-1]) # output : [2,3,"a","b"]
print()  #empty line

#  Change Item Value
# To change the value of a specific item, refer to the index number:

print(B)
B[2] = "newval"
print(B)
print()  #empty line

#  Change a Range of Item Values
# To change the value of items within a specific range,
# define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

print(B)
new_list = [4,7,8]
B[2:5] = new_list
print(B)
print()  #empty line

#  Note: The length of the list will change when the number of items inserted does not match the number of items replaced.

# Add List Items

#  Append Items
# To add an item to the end of the list, use the append() method:

print(B)
B.append("12")
print(B)
print()  #empty line

#  Insert Items
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:

print(B)
B.insert(2, "insert")
print(B)
print()  #empty line

#  Extend List
# To append elements from another list to the current list, use the extend() method.

C=[9,8,"k"]
print(B)
B.extend(C)
print(B)
print()  #empty line

#  Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

D=("i",'j',12)
print(B)
B.extend(D)
print(B)
print()  #empty line

# Remove List Items

#  Remove Specified Item
# The remove() method removes the specified item.

print(B)
B.remove("insert")
print(B)
print()  #empty line

#  Remove Specified Index
# The pop() method removes the specified index.

print(B)
B.pop(2)
print(B)
print()  #empty line

# If you do not specify the index, the pop() method removes the last item.

# The del keyword also removes the specified index:
print(B)
del B[2]
print(B)
print()  #empty line
# The del keyword can also delete the list completely.

#  Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.

print(C)
C.clear()
print(C)
print()  #empty line

#                                      *** ( loop in list & List Comprehension )  in loop section ***

# Sort Lists

#  Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

L = ['z','s','c','a','b','o','t','A','Z']
L.sort()
print(L)
print()  #empty line

#  Sort Descending
# To sort descending, use the keyword argument reverse = True:

L = ['z','s','c','a','b','o','t','A','Z']
L.sort(reverse=True)
print(L)
print()  #empty line

#  Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.
# The function will return a number that will be used to sort the list (the lowest number first):

#  Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Luckily we can use built-in functions as key functions when sorting a list.
# So if you want a case-insensitive sort function, use str.lower as a key function:

L = ['z','s','c','a','b','o','t','A','Z']
L.sort(key = str.lower)
print(L)
print()  #empty line

#  Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?
# The reverse() method reverses the current sorting order of the elements.

L = ['z','s','c','a','b','o','t','A','Z']
L.reverse()
print(L)
print()  #empty line