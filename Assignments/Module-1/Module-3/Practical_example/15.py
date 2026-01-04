class lipstick:
    l_shade: int
    l_brand: str

    def l_getdata(self):
        self.l_shade = int(input("Enter lipstick shade number: "))
        self.l_brand = input("Enter lipstick brand: ")

class foundation:
    f_type: str
    f_brand: str

    def f_getdata(self):
        self.f_type = input("Enter foundation type: ")
        self.f_brand = input("Enter foundation brand: ")

class mascara:
    m_length: int
    m_brand: str

    def m_getdata(self):
        self.m_length = int(input("Enter mascara length in mm: "))
        self.m_brand = input("Enter mascara brand: ")


class makeup(lipstick, foundation, mascara):
    def printdata(self):
        print("------------LIPSTICK DATA-------------")
        print("Lipstick Shade Number:", self.l_shade)
        print("Lipstick Brand:", self.l_brand)
        print("------------FOUNDATION DATA-------------")
        print("Foundation Type:", self.f_type)
        print("Foundation Brand:", self.f_brand)
        print("------------MASCARA DATA-------------")
        print("Mascara Length (mm):", self.m_length)
        print("Mascara Brand:", self.m_brand)

mp = makeup()
mp.l_getdata()      
mp.f_getdata()
mp.m_getdata()
mp.printdata()

    