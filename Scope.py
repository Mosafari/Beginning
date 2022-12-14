# Scope

# A variable is only available from inside the region it is created. This is called scope.

# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
x=1
y=2
def myfunc():
  x = 300
  print(x,y)

myfunc() 
print(x)
# x is local inside the myfunc
# we can use y inside myfunc because its global

# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.

# Naming Variables
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables,
# one available in the global scope (outside the function) and one available in the local scope (inside the function)

# Global Keyword
# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.
# The global keyword makes the variable global.

# Also, use the global keyword if you want to make a change to a global variable inside a function.