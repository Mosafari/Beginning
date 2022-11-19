# Try Except

# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
# These exceptions can be handled using the try statement

# Since the try block raises an error, the except block will be executed.
# Without the try block, the program will crash and raise an error

x =6
y = 0
try:
    print(x/y)
except Exception as e:
    print(e)
    
try:
    print(notexist)
except:
    print("Something went wrong")
else:
    print("else doesn't execute")
    
# Else
# You can use the else keyword to define a block of code to be executed if no errors were raised

try:
    print(x)
except:
    print("Something went wrong")
else:
    print("elseeeeeeeee")
    
# Finally
# The finally block, if specified, will be executed regardless if the try block raises an error or not.
    
try:
    print(y)
except:
    print("Something went wrong")
else:
    print("elseeeeeeeee")
finally:
    print("tadaaaa")
    