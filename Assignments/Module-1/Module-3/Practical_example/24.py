import re
mystr="This is nice resturant."
x=re.match("nice",mystr)
print(x)

if x:
    print("Yes! We have a match")
else:
    print("No match")