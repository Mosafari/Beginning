import math as M

print("what do you want to do ??  #help(sin,cos,+,-,/ for divide,x for multi,% for rest ,and 0 for Exit)")
x=input()
def calculator(char) :
    if x == "sin":
        a=M.sin(int(input()))
        print(a)
    elif x == "cos":
        b=M.cos(int(input()))
        print(b)
    elif x == "+":
        c=int(input("num1:"))
        d=int(input("num2 :"))
        print(c+d)
    elif x == "-":
        e=int(input("num1:"))
        f=int(input("num2 :"))
        print(e-f)
    elif x == "x":
        g=int(input("num1:"))
        h=int(input("num2 :"))
        print(g*h)
    elif x == "/":
        i=int(input("num1:"))
        j=int(input("num2 :"))
        print(i/j)
    elif x == "%":
        k=int(input("num1:"))
        l=int(input("num2 :"))
        print(k%l)
    elif x=='0'   :
        pass
    else:   
        print("i dont know what is that")
      
while x!=0 :
    calculator(x)      
    if x=='0':
        print('Bye(:')
        break
    print('what next!?')
    x=input()
    if x=='0':
        print('Bye:)')
        break
      