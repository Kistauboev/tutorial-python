class Shape:
    def __init__(self):
        pass 

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
