
#method overriding--same method,same para classes different
class A:
    def get(self):
     self.a=int(input("enter the value of a"))
class B(A):
    def get(self):
        self.b=int(input("enter the value of a")) 
        super().get()  #accessing parent class data
    def addition(self):
        result=self.a+self.b
        print(result)   
b=B()
b.get()
b.addition() 