#Calculator
import math
def calculator(x,y):
    print("select an operation :-")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Exponent")
    a=int(input("Choose from 1/2/3/4/5/6 :"))
    if a==1:
        print(x,"+",y,"=",x+y)
    elif a==2:
        print(x,'-',y,'=',x-y)
    elif a==3:
        print(x,'x',y,'=',x*y)
    elif a==4:
        print(x,'divided by',y,'=',x%y)
    elif a==5:
        print("Square root of",x,'=',math.sqrt(x))
    elif a==6:
        print(x,'to the power',y,'=',x**y)
    else:
        print("Invalid Input")
try:
    while True:
        num1=int(input("enter 1st no.:"))
        num2=int(input("enter 2nd no.:"))
        calculator(num1,num2)
        nextcal=input("Do you want to continue(yes/no):")
        if nextcal=="no":
            print("THANK YOU")
            break
except:
    if False:
        print("Invaild")
