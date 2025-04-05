class employee:
    def getdata(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def disp(self):
        print("name is ",self.name)    
        print("age is ",self.age)
        print("salary is ",self.salary)
class contract_emp(employee):
    def getbonus(self,bonus):
         self.bonus=bonus
         print("bonus is",bonus)
print("employee calling")         
em=employee()
em.getdata("harry",23,4535346)
em.disp()
print("contract empp calling.....")
ce=contract_emp()
ce.getdata("ram",20,213243)
ce.getbonus(5000)
ce.disp()