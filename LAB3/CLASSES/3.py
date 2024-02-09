class Shape:
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, uzunlik, eni):
        super().__init__()  # Ota sinfning konstruktorini chaqirish
        self.uzunlik = uzunlik
        self.eni = eni

    def hisoblash(self):
        return self.uzunlik * self.eni
