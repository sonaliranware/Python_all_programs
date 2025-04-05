#hierachiacl inheritance------
class grandfather:
    def farm(self):
        print("farming...")
class father(grandfather):
    def house(self):
        print("house....")
class child(grandfather):
    def car(self):
        print("car...")
f=father()
f.farm()
f.house()        
c=child()
c.car()
c.farm()                        
