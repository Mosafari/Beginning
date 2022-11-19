# Conditions and If statements

# Python supports the usual logical conditions from mathematics:

#     Equals: a == b
#     Not Equals: a != b
#     Less than: a < b
#     Less than or equal to: a <= b
#     Greater than: a > b
#     Greater than or equal to: a >= b

# These conditions can be used in several ways, most commonly in "if statements" and loops.

# An "if statement" is written by using the if keyword.

a = 33
b = 200
if b > a:
  print("b is greater than a")
print() #empty line

# Indentation
# ***Python relies on indentation (whitespace at the beginning of a line) to define scope in the code.
# Other programming languages often use curly-brackets for this purpose. ***

#elif

x = 5
y = 5

if x > y:
    print("x  greater than  y")
elif x == y :
    print('x equal to  y')
print() #empty line

#else

x = 5
y = 3

if x > y:
    print("x greater than  y")
elif x == y :
    print('x equal to  y')
else :
    print('y greater than  x')
print() #empty line

# The else keyword catches anything which isn't caught by the preceding conditions

# Short conditions
# If you have only one statement to execute, you can put it on the same line as the if statement.

j =6
k =7
if j<k : print("k is greater")
print() #empty line

#short if-else
print('j') if j>k else print("k")
print() #empty line

# This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") 
print() #empty line
