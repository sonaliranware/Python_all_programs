def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b            
print("my simple calculator")    
options={1:'Add',2:'sub',3:'mul',4:'div',5:'quit'}
while True:
    print("\n\n 1.Addition")
    print("2.substraction")
    print("3.multiplication")
    print("4.division")
    print("5.Quit")
    choice=int(input("enter your choice "))
    if choice not in options:
        print("invalid choice please re-enter")
        continue
    if choice==5:
        print(" bye....")   
        break 
    else:
        n1=int(input("enter first  number"))
        n2=int(input("enter second number"))
    if choice==1:
        r1=add(n1,n2)
        print("addition is ",r1)     
    elif choice==2:
        r2=sub(n1,n2)
        print("substraction is ",r2)     
    elif choice==3:
        r3=mul(n1,n2)
        print("multiplication is ",r3) 
    elif choice==4:
        r4=div(n1,n2)
        print("division is ",r4)  
                