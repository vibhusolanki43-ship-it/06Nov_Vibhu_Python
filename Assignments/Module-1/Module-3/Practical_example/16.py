class Makeup:
    def brand_info(self):
        print("Makeup Product Information")


class Lipstick(Makeup):
    def getdata(self):
        self.l_shade = int(input("Enter lipstick shade number: "))
        self.l_brand = input("Enter lipstick brand: ")

    def printdata(self):
        print("\n------ LIPSTICK DATA ------")
        print("Shade Number:", self.l_shade)
        print("Brand:", self.l_brand)


class Foundation(Makeup):
    def getdata(self):
        self.f_type = input("Enter foundation type: ")
        self.f_brand = input("Enter foundation brand: ")

    def printdata(self):
        print("\n------ FOUNDATION DATA ------")
        print("Type:", self.f_type)
        print("Brand:", self.f_brand)


class Mascara(Makeup):
    def getdata(self):
        self.m_length = int(input("Enter mascara length in mm: "))
        self.m_brand = input("Enter mascara brand: ")

    def printdata(self):
        print("\n------ MASCARA DATA ------")
        print("Length (mm):", self.m_length)
        print("Brand:", self.m_brand)


# Objects of child classes
lip = Lipstick()
lip.getdata()
lip.printdata()

found = Foundation()
found.getdata()
found.printdata()

mas = Mascara()
mas.getdata()
mas.printdata()
mas.brand_info()
