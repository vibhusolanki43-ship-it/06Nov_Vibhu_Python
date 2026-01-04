#method_ovrerride
class Animal:
    def getdata(self,name):
        print("Animal Name:",name)

    def getdata(self,species):
        print("Animal Species:",species)


an=Animal()
an.getdata("lion")     
an.getdata("dog")


#method_overrinding

class vehicle:
    def getdata(self,brand,model):
        print("Vehicle Brand:",brand)
        print("Vehicle Model:",model)

class car(vehicle):
    def getdata(self,brand,model,year):
        print("Car Brand:",brand)
        print("Car Model:",model)
        print("Car Year:",year)

class bike(vehicle):
    def getdata(self,brand,model,type):
        print("Bike Brand:",brand)
        print("Bike Model:",model)
        print("Bike Type:",type)

c=car()
c.getdata("Toyota","Camry",2020)    
