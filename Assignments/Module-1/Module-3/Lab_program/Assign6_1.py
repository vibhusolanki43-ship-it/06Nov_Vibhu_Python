class school:

    t_id: int
    t_name: str
    t_sub: str

    def getdata(self):
        self.t_id = input("Enter teacher id:")
        self.t_name = input("Enter teacher name:")
        self.t_sub = input("Enter teacher subject:")
    
    def printdata(self):
        print("Teacher id:", self.t_id)
        print("Teacher name:", self.t_name)
        print("Teacher subject:", self.t_sub)
    
sc = school()
sc.getdata()    
sc.printdata()

    