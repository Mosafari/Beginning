# JSON

# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# If you have a JSON string, you can parse it by using the json.loads() method -> The result will be a Python dictionary.

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"]) 


# to convert Python object into a JSON string we can use the json.dumps() method.

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)

print(y) 

# we can Use the indent parameter to define the numbers of indents
print(json.dumps(x, indent=4))

# more about JSON on : https://www.w3schools.com/python/python_json.asp