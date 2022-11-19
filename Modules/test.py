# What is a Module?

# Consider a module to be the same as a code library.
# A file containing a set of functions you want to include in your application.

# Create a Module
# To create a module just save the code you want in a file with the file extension .py

# Use a Module
# Now we can use the module we just created, by using the import statement

from power2 import powertwo as p2

print(p2(4))

# Naming a Module

# You can name the module file whatever you like, but it must have the file extension .py
# Re-naming a Module

# You can create an alias when you import a module, by using the as keyword

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like

# Using the dir() Function
# There is a built-in function to list all the function names (or variable names) in a module. The dir() function

print(dir())

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]
