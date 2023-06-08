class Dimension:
    def __init__(self, o=None):
        self.width = 0
        self.height = 0
        self.x = 0
        self.y = 0

    def getArea(self):
        area = self.width * self.height
        return area

    def reconfigure(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def toString(self):
        string = f'width: {self.width} height: {self.height} x: {self.x} y: {self.y}'
        return string
