class music:
    def getdata(self,type,name):
        print(f"Music Type: {type}, Name: {name}")   

class genre(music):
    def getdata(self,type,name):
        return super().getdata(type,name)
    
class artist(music):
    def getdata(self,type,name):
        return super().getdata(type,name)
    
g=genre()
g.getdata("Rock","Queen")

a=artist()
a.getdata("Pop","Adele")


