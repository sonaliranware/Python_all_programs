'''polymorphism----greek word
poly--many/multiple 
morphism---form
ability to take more than one form
2 types
metod overloading-----(not support)---same method,different para,same class
method overriding----(python support)---same method,same para but classes different '''
#constructor overriding ----same constructor name,same parameter but different classes
class A:
    def __init__(self):
     self.a=int(input("enter the value of a"))
class B(A):
    def __init__(self):
        self.b=int(input("enter the value of a")) 
        super().__init__()  #accessing parent class data
    def addition(self):
        result=self.a+self.b
        print(result)   
b=B()
b.addition()              