'''inheritance---
create new class with the
 help of properties of the
  base
IS-A relation ship
provide code reusability and code optimization
syntax:
class subclass(superclass) 
'''
class father:
        def farm(self):
         print("farm.....")
class child(father):    #inheritance
    def house(self):
        print("house")

c=child()
c.farm()
c.house()        
