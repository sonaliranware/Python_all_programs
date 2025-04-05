'''data abstarction---- hiding internal details and showing 
main  functionality
concreat method---actual method execution
abstarct method----method declaration only
so we cant create object of abstarct class
'''
class fruits:             #abstract base class(ABC) 
    def taste(self):     #abstarct method
        pass
    def color(self):
        pass
class apple(fruits):
     def taste(self):
        print("tangy")
     def color(self):
        print("red")   
class Mango(fruits):
    def taste(self):
        print("sweet")
    def color(self):
        print("yellow")
a=apple()
a.taste()
a.color()
m=Mango()
m.taste()
m.color()        
