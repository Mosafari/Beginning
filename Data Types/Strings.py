# Multiline Strings
#  You can assign a multiline string to a variable by using three quotes:

A = """Hello,
       World!
       Python
       is 
       fun"""
       
print(A)
print()  #empty line

# Strings are Arrays
#  Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.
#  However, Python does not have a character data type, a single character is simply a string with a length of 1.
#  Square brackets can be used to access elements of the string.

print(A[1]) # output: "e"    !!!(indexes start from 0)!!!
print()  #empty line

# Looping Through a String

B = "Python"

for i in B:
    print(i)
    
# String Length

print(len(B))  # output: 6
print()  #empty line

# Membership using in or not in

print("Py" in B) # output: True
print()  #empty line