# Dates

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects

import datetime

x = datetime.datetime.now()
print(x) 

# Date Output

# When we execute the code from the example above the result will be:
# 2022-11-19 18:55:00.836964
# The date contains year, month, day, hour, minute, second, and microsecond.
# The datetime module has many methods to return information about the date object.

# The datetime module supplies classes for manipulating dates and times.

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.
# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) 

# While date and time arithmetic is supported,
# the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.
#  more about datetime on : https://docs.python.org/3/library/datetime.html
# and : https://www.w3schools.com/python/python_datetime.asp