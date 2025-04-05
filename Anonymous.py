'''Anonymous.py
Anonymous function--- function having without name
this is also known as lambda function
syntax:
lambda (parameter):
    code
'''
#by using normal function
def square(n):
    return n*n
print("square is",square(5))    

#by using lambda function
result=lambda n:n*n
print("square by using lambda",result(2))

#addition of 3 numbers using lambda

#map function---execute the given function with iterables(lits,tuple)
#map(func, *iterables) --> map object
def square(n):
    return n*n

t=(1,2,3,4,5)
result=map(square,t)
r1=set(result)
print(r1)

r5=map(lambda m:m*m,t)
print("using lambda with map function",set(r5))


#reduce function---inbuilt function in python
#applies on iterable items
# reduce result into single value
from functools import reduce
def addition(a,b):
    return a+b
L=(1,2,3,4,5)
r2=reduce(addition,L)
print(r2)     

mylist=[10,20,30,40,50]
r6=reduce(lambda x,y:x if x>y else y,mylist)
print("greater value is",r6)


number=[1,2,3,4,-9,-7]
r7=filter(lambda x:x<=0,number)
print(list(r7))

#remove duplicate ele in list
number2=[1,2,3,4,3,2,1,6,7]
r8=filter(lambda x:number2.count(x)==1,number2)
print(list(r8))











