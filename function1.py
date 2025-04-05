'''function---
it is block of code /statements
when you want to execute this block of statment n number of times
then we can call function
adv--code reuability
    code optimization/code minimization
synatax:
     def function_name(parameter):
         function body
its compulsory to call that function
how we call function?
function_name()              
'''
def greetmsg():
    print("hello good morning......")
    print("welcome in python")
    print("welcome in django.....")

greetmsg()  
greetmsg()  
greetmsg()
greetmsg()

def cube(x): #function declarations
    result=x*x*x       #function body
    print(result)
cube(5)    #calling function

def cube1(n):
    return n*n*n


print("cube is ",cube1(5))
print("cube is ",cube1(4))
print("cube is ",cube1(2))


