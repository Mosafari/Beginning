# Boolean Values
#  In programming you often need to know if an expression is True or False.
#  You can evaluate any expression in Python, and get one of two answers, True or False.
#  When you compare two values, the expression is evaluated and Python returns the Boolean answer:

print(2<3)
print(5>9)
print(2==2)
print()  #empty line

# Evaluate Values and Variables
#  The bool() function allows you to evaluate any value, and give you True or False in return :

print(bool("python"))
print(bool(12))
print(bool([1])) # list with one element
print(bool([])) # empty list
print(bool(0))
print(bool(""))
print()  #empty line

# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones

#  In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "",
# the number 0, and the value None. And of course the value False evaluates to False.