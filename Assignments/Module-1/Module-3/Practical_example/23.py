import re
mystr="today is sunday."
x=re.search("sunday",mystr)
print(x)

if x:
    print("Yes! We have a match")       
else:
    print("No match")
