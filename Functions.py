# Functions

# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the def keyword
    
# Calling a Function
# To call a function, use the function name followed by parenthesis

# Arguments

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.

def Greeteng(name):
    print("hello, ", name)
    print() #empty line
    
Greeteng("ali")

# Arguments are often shortened to args in Python documentations.

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments,
# you have to call the function with 2 arguments, not more, and not less. 

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed
# into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def Greeteng2(*names):
    for name in names:
        print("hello, ", name)
    print() #empty line
    
Greeteng2("ali",'mohamad','reza')

# Arbitrary Arguments are often shortened to *args in Python documentations.

# Keyword Arguments
# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def Greeteng3(name1,name2,name3):
    print("hello, ", name3)
    print("hello, ", name2)
    print("hello, ", name1)
    print() #empty line
    
Greeteng3(name2='ali',name1='mohamad',name3='reza')