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

