class Dimension:
    def __init__(self, x=0, y=0, width=0, height=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def getArea(self):
        return self.width * self.height

    def reconfigure(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def toString(self):
        return f"width: {self.width}, height: {self.height}, x: {self.x}, y: {self.y}"
