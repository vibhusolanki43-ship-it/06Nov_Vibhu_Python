Nursury_name="Green Leaf Nursury"

class flower:
    def getdata(self):
        self.color = input("Enter the color of the flower: ")
        self.type = input("Enter the size of the flower: ")

        print("Nursury Name:", Nursury_name)
        print("Flower Color:", self.color)
        print("Flower Size:", self.type)

flw = flower()
flw.getdata()   


    