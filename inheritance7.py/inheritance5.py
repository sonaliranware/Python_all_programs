#multiple inheritance------
class grandfather:
    def farm(self):
        print("farming...")
class father:
    def house(self):
        print("house....")
class child(father,grandfather):
    def car(self):
        print("car...")
c=child()
c.car()
c.house()
c.farm()