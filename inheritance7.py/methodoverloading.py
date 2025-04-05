#method overloading--same method,same class but different para
#but python not support method overloading because it gives
# missing  required positional argument error
class A:
    def addition(self,a,b):
        self.a=a
        self.b=b
        r1=self.a+self.b
        print(r1)
    def addition(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        r1=self.a+self.b+self.c
        print(r1)
a=A()
a.addition(10,20) 
a.addition(10,20,30)       