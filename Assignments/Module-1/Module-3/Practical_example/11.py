class movie:
    m_name=str
    m_director=str
    m_year=int
    m_rating=float

    def getdata(self):
        self.m_name=input("Enter movie name:")
        self.m_director=input("Enter movie director:")
        self.m_year=int(input("Enter movie release year:"))
        self.m_rating=float(input("Enter movie rating (out of 10):"))

    def printdata(self):
        print("Movie Name:",self.m_name)
        print("----------------------------")
        print("Director:",self.m_director)
        print("----------------------------")
        print("Release Year:",self.m_year)
        print("----------------------------")
        print("Rating:",self.m_rating)

mv=movie()
mv.getdata()
mv.printdata()
