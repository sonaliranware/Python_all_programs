'''local variable---variable which is declared inside the function
and scope limited only that function we cant access outside
global variable-- access inside and outside the function'''


def msg():
    s="local scope"     # local variable
    print(s)
    print(k)

k="global scope"
print(k)  
msg()  