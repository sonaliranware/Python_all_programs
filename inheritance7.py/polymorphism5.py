class itvedant:
    def training(self):
        print("training itvdept")
    def placement(self):
        print("placement itvdept")
class itvedantEclass(itvedant):
    def training(self):
        print("training edept")
    def placement(self):
        print("placement edept")
class itvedantThane(itvedant):
    def training(self):
        print("training Tdept")
    def placement(self):
        print("placement Tdept")        
i=itvedant()
ie=itvedantEclass()
ip=itvedantThane()  
for obj in (i,ie,ip):
    obj.training()
    obj.placement()