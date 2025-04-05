#program for class object and function
class student:
    def getdata(self,id,name,age):#parameterized
        self.id=id
        self.name=name
        self.age=age
    def disp(self):
        print("id id ",self.id)
        print("name is ",self.name)
        print("age is ",self.age)
s=student()
s.getdata(10,'harry',30)#pass actual values
s.disp()  






