# RegEx

# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.

# RegEx can be used to check if a string contains the specified search pattern.
# RegEx Module

# Python has a built-in package called re, which can be used to work with Regular Expressions.

zen = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

import re

a = re.findall("is",zen)
print(len(a))
print() #empty line

b = re.sub("\s","--", zen)
print(b)
print() #empty line

c = re.split("is",zen)
print(c)
print() #empty line

t = re.split('\n',zen)
print(t)
print() #empty line

for i in t:
    d = re.search("^If.*idea\.$",i)
    if d:
        print(i)