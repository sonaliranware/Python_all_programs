'''recursion function---
we can call function within same function this is known as recursion function

 syntax:
 def function_name():
    function_name()
    
def hello():
    hello()    '''

#find factorial of number using recursion
def fact(n):
    if n==1:
        return 1
    else:                     #2
        return (n*fact(n-1))   #2*fact(2-1)

print("factorial is ",fact(5))