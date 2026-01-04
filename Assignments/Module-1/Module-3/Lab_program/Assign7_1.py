#single Inheritance
class bookstore:

    book:str
    price:float
    author:str

    def getdata(self):
        self.book=input("Enter book name:")
        self.price=float(input("Enter book price:"))
        self.author=input("Enter author name:")

class novel(bookstore):

    def printdata(self):
        print("Book Name:",self.book)
        print("Book Price:",self.price)
        print("Author Name:",self.author)   

n=novel()
n.getdata() 
n.printdata()

#multiple Inheritance

class lion:
    lname:str
    lage:int

    def l_getdata(self):
        self.lname=input("Enter lion name:")
        self.lage=int(input("Enter lion age:"))

class tiger:
    tname:str
    tage:int

    def t_getdata(self):
        self.tname=input("Enter tiger name:")
        self.tage=int(input("Enter tiger age:"))

class bear:
    bname:str
    bage:int

    def b_getdata(self):
        self.bname=input("Enter bear name:")
        self.bage=int(input("Enter bear age:"))

class zoo(lion,tiger,bear):

    def printdata(self):
        print("------------LION'S DATA-------------")
        print("Lion's name:",self.lname)
        print("Lion's age:",self.lage)
        print("------------TIGER'S DATA-------------")
        print("Tiger's name:",self.tname)
        print("Tiger's age:",self.tage)
        print("------------BEAR'S DATA-------------")
        print("Bear's name:",self.bname)
        print("Bear's age:",self.bage)

z=zoo()
z.l_getdata()   
z.t_getdata()
z.b_getdata()
z.printdata()

#multilevel Inheritance

class college:
    cname:str
    cloc:str

    def c_getdata(self):
        self.cname=input("Enter college name:")
        self.cloc=input("Enter college location:")

class department(college):
    dname:str
    dhead:str

    def d_getdata(self):
        self.dname=input("Enter department name:")
        self.dhead=input("Enter department head:")
    
class course(department):
    coursename:str
    duration:int

    def co_getdata(self):
        self.coursename=input("Enter course name:")
        self.duration=int(input("Enter course duration in years:"))

class university(course):
    def printdata(self):
        print("------------COLLEGE'S DATA-------------")
        print("College Name:",self.cname)
        print("College Location:",self.cloc)
        print("------------DEPARTMENT'S DATA-------------")
        print("Department Name:",self.dname)
        print("Department Head:",self.dhead)
        print("------------COURSE'S DATA-------------")
        print("Course Name:",self.coursename)
        print("Course Duration (in years):",self.duration)
    


u=university()
u.c_getdata()       
u.d_getdata()
u.co_getdata()
u.printdata()