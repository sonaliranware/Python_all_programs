def swap(a,b):
    print("before swappig",a,b)#10 20
    a=a+b #a=10+20=30
    b=a-b#30-20=10
    a=a-b#30-10=20
    print("after swapping",a,b)#20  10
n1=int(input("enter value of a"))#10
n2=int(input("enter value of b"))#20
swap(n1,n2)    
