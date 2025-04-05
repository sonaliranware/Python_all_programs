'''types of inheritance
1)single inheritance
2)multilevel inheritance
3)hirachical inhe
4)multiple inhe
5)hybrid inhe '''
#multilevel inheritance------
class grandfather:
    def farm(self):
        print("farming...")
class father(grandfather):
    def house(self):
        print("house....")
class child(father):
    def car(self):
        print("car...")
c=child()
c.car()
c.house()
c.farm()                        

