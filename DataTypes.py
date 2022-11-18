#variables : Variables are containers for storing data values. like : x,y,z,A_a,BreakingBad, ...
# You can get the data type of any object by using the type() function.

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