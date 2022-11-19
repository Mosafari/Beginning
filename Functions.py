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
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function(**kid):
  print("His last name is " + kid["lname"])
  print() #empty line

my_function(fname = "Tobias", lname = "Refsnes") 

# Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.

# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

def Greeteng4(name='noname'):
    print("hello, ", name)
    print() #empty line

Greeteng4()
Greeteng4("ali")

# **** ou can send any data types of argument to a function (string, number, list, dictionary etc.),
# and it will be treated as the same data type inside the function.
# E.g. if you send a List as an argument, it will still be a List when it reaches the function ****
