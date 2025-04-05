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

id=int(input("enter your id"))
name=input("enter name")
age=int(input("enter age"))
s.getdata(id,name,age)
s.disp() 
