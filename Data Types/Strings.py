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