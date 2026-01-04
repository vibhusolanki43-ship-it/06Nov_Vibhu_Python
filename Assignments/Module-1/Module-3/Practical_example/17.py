class Makeup:
    def common_info(self):
        print("Makeup Product Details")


class Lipstick(Makeup):
    def l_getdata(self):
        self.l_shade = int(input("Enter lipstick shade number: "))
        self.l_brand = input("Enter lipstick brand: ")


class Foundation(Makeup):
    def f_getdata(self):
        self.f_type = input("Enter foundation type: ")
        self.f_brand = input("Enter foundation brand: ")


class Mascara(Lipstick, Foundation):
    def m_getdata(self):
        self.m_length = int(input("Enter mascara length in mm: "))
        self.m_brand = input("Enter mascara brand: ")

    def printdata(self):
        print("\n-------- LIPSTICK DATA --------")
        print("Shade Number:", self.l_shade)
        print("Brand:", self.l_brand)

        print("\n-------- FOUNDATION DATA ------")
        print("Type:", self.f_type)
        print("Brand:", self.f_brand)

        print("\n-------- MASCARA DATA ---------")
        print("Length (mm):", self.m_length)
        print("Brand:", self.m_brand)


# Object creation
ms = Mascara()

ms.l_getdata()
ms.f_getdata()
ms.m_getdata()
ms.printdata()
ms.common_info()