# For Loops

# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

A = "string"
B = 5 #num
C = ['a','b','c','d','e','f']
D = (2,4,6,8,10)
E = {1,1,2,3,4,5}
F = {'a':1, 'b':2, 'c':3, 'd':4}

# The for loop does not require an indexing variable to set beforehand.

# loop through string
for char in A :
    print(char)
    
print() #empty line
    
# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments by 1 (by default), and ends at a specified number.

for i in range(B):
    print(i)
    
print() #empty line



# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
# The range() function defaults to 0 as a starting value,
# however it is possible to specify the starting value by adding a parameter: range(2, 6),
# which means values from 2 to 6 (but not including 6):

for i in range(2,9):
    print(i)
    
print() #empty line

# The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):

for i in range(0,11,2):
    print(i)
    
print() #empty line

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

for i in range(B):
    print(i)
else:
    print("end")
print() #empty line

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop":

for i in range(1,11):
    for j in range(1,11):
        print('{:10}'.format(i*j),end="")
    print()

print('_'*80) #empty line

for i in range(1,11):
    for j in range(1,11):
        if i >= j : print("{:5}".format('O') ,end='') 
    print()