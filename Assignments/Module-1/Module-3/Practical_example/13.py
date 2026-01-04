class biscuit:
    def getdata(self):
        self.name = input("Enter the name of the biscuit: ")
        self.flavor = input("Enter the flavor of the biscuit: ")
        self.price = float(input("Enter the price of the biscuit: "))

class backry(biscuit):
    def printdata(self):
        print("Biscuit Name:", self.name)
        print("Biscuit Flavor:", self.flavor)
        print("Biscuit Price:", self.price)

b = backry()
b.getdata()
b.printdata()
