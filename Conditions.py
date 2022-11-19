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

