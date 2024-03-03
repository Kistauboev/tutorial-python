import os

path = r'C:\PYTHON\LAB 5'
for i in range(65,91):
    name = os.path.join(path, chr(i) + ".txt")
    f = open(name, "a")