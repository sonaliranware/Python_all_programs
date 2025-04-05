#program for class object and function
class student:
    id=100
    name="harry"
    age=20
    def getdata(self):
        print("id id ",self.id)
        print("name is ",self.name)
        print("age is ",self.age)
s=student()
s.getdata()        