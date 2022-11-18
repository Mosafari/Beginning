#variables : Variables are containers for storing data values. like : x,y,z,A_a,BreakingBad, ...

# Numbers
x = 13 #int
y= 24.5 #float
k= 1j #complex

z= 'hello, ' #string
h= "world!"

i=False #boolean

a= [1,2,3.4,'a','b'] # list to store string and int/float list, ...
b= ( 1,2,3.4,'a' 'b') # tuple to store string & int/float list, ... (imutable)
c = {'one': 1,2:'two'} #dict key(imutable): value paires to store val and accses with [key]
d={1,2,3,4,4,4,'a','b','c'} #set to store string and int/float ... (Ignores duplicate values)

n= None #Nonetype



# Output Variables
# The Python print() function is often used to output variables.

print(x) #int
print(y) #float
print(k) #complex

print()  #empty line

print(z) 
print(h)
print(z+h) #print hello, world! in one line

print()  #empty line

#Specify a Variable Type
# There may be times when you want to specify a type on to a variable. This can be done with casting.
# Casting in python is therefore done using constructor functions: int(), float(), complex(), ...
# You can get the data type of any object by using the type() function.
 
print(x) #int
print(float(x)) # x as float
print(complex(x)) # x as complex

print()  #empty line

print(type(x),type(float(x))) 

print()  #empty line

print(int(y)) # y as int
print(y) # float
print(complex(y)) # y as complex

print()  #empty line

print(int(k.real)) # k as int (using .real for real part)
print(float(k.real)) # k as float (using .real for real part)
print(k) # complex

print()  #empty line

g = "5" # number as string

print()  #empty line

print(g + " type of g: "+type(g))
print(int(g)) # g as int
print(str(x)) # x as str

# You can convert str to int, float if it was all numeric !!!!