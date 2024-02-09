class String:
    def __init__(self):
        pass #self.string = " "

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

x = String()
x.getString()
x.printString()
