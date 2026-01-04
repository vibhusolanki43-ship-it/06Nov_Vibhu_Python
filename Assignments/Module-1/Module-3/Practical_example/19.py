class tv:
    def getdata(self,brand):
        self.brand=brand
        print("Brand:",self.brand)

    def getdata(self,price):
        self.price=price
        print("Price:",self.price)

t=tv()
t.getdata("LGTV")     
t.getdata(45000)    

        