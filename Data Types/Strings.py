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

# Slicing Strings
#  You can return a range of characters by using the slice syntax.

#Note: The first character has index 0.
print(B[1:4]) # output: "yth" 
print(B[:4]) # Slice From the Start
print(B[2:]) # Slice To the End
print(B[-1:-3]) # Negative Indexing
print()  #empty line

# Modify Strings
#  Python has a set of built-in methods that you can use on strings.

C = "HELLO, world"
print(C.upper()) # output: "HELLO, WORLD"  Upper Case
print(C.lower()) # output: "hello, world"  Lower Case
print(C.strip()) # output: "HELLO, world"  Remove Whitespace
print(C.replace("H", "J")) # output:  "JELLO, world"  Replace String
print(C.split(",")) # output :  ['HELLO', ' world']  Split String
print()  #empty line

# String Format

"""we cannot combine strings and numbers like this:
    num = 2
    txt = "it doesn't work {}" + age
    print(txt)""" # output: Error
    
#  The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
    
num1 = 100
num2 = 200
num3 = 300
txt = "now it works {}"
print(txt.format(num1))
print()  #empty line
#  You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

txt2 = "num1 : {0}, num3 : {2}, num2 : {1}"
print(txt2.format(num1, num2, num3))
print()  #empty line

# Escape Character
#  To insert characters that are illegal in a string, use an escape character.
#  An escape character is a backslash \ followed by the character you want to insert.

print("Special cases aren't special enough to break the rules.")
print('Special cases aren\'t special enough to break the rules.') # output : Special cases aren't special enough to break the rules.
# Other escape characters : https://www.w3schools.com/python/python_strings_escape.asp
print()  #empty line


# String Methods
#  Python has a set of built-in methods that you can use on strings.
# Note: All string methods return new values. They do not change the original string.
H= "Programming is fun"
print(H.count("m")) # output : 2
print(H.find("r")) # output : 1 (index 1)  Searches the string for a specified value and returns the position of where it was found (first one)
# more details on : https://www.w3schools.com/python/python_strings_methods.asp
print()  #empty line

