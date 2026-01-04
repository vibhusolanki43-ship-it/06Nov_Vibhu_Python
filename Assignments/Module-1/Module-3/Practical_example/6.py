file = open("school.txt", "r")
data = file.read(10)
print("Data read:", data)
position = file.tell()
print("Current file cursor position:", position)

