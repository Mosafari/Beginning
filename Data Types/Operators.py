# Python Operators
#  Operators are used to perform operations on variables and values.

# Python Arithmetic Operators

print(4/2) # output : 2.0
print(4//2) # output : 2
print(6-2) # output : 4
print(2+4) # output : 6
print(4*2) # output : 8
print(4**2) # output : 16
print()  #empty line

# Python Assignment Operators
#  Assignment operators are used to assign values to variables:
x = 4
print(x) # output : 4
x+=2 # x = x + 2 -> 4 + 2 = 6  -> x = 6
print(x) # output : 6
x-=4 # x = x - 2 -> 6 - 4 = 2 -> x = 2
print(x) # output : 2
x*=2 # x = x * 2 -> 2 * 2 = 4 -> x = 4
print(x) # output : 4
print()  #empty line

# Python Comparison Operators
#  Comparison operators are used to compare two values:

a = 3
b = 7
print(a==b) # output : False
print(a!=b) # output : True
print(a<b) # output : True
print(a>b) # output : False
print()  #empty line

# Python Logical Operators
#  Logical operators are used to combine conditional statements: (and, or, not)

print(a<b and a!=b) # output : True  (Returns True if both statements are true)
print(a<b and a==b) # output : False
print(a<b or a==b) # output : True
print(not a==b) # output : True
print()  #empty line

# Python Identity Operators
#  Identity operators are used to compare the objects,
#  not if they are equal, but if they are actually the same object, with the same memory location:

print(a is b) # output : False
print(a is not b ) # output : True
print()  #empty line