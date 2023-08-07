from dimension import Dimension

class Rectangle(Dimension):
    def __init__(self, o=None):
        super().__init__(o)
        self.r = 255
        self.g = 255
        self.b = 255
        self.a = 255
        self.borderR = 0
        self.borderG = 0
        self.borderB = 0
        self.borderWidth = 1
        self.method = 'fill'
        self.useBorder = True

    def init(self, x, y, width, height, method, useBorder):
        self.x = x or 0
        self.y = y or 0
        self.width = width or 0
        self.height = height or 0
        self.method = method or self.method
        self.useBorder = useBorder or self.useBorder

    def setColor(self, r, g, b, a):
        self.r = r or self.r
        self.g = g or self.g
        self.b = b or self.b
        self.a = a or self.a

    def setBorderColor(self, r, g, b):
        self.borderR = r or 0
        self.borderG = g or 0
        self.borderB = b or 0

    def draw(self):
        _r, _g, _b, _a = canvas:attrColor()
        canvas:attrColor(self.r, self.g, self.b, self.a)
        canvas:drawRect(self.method, self.x, self.y, self.width, self.height)
        if self.useBorder:
            self.drawBorder()
        canvas:attrColor(_r, _g, _b, _a)
        canvas:flush()

    def drawBorder(self):
        if self.borderWidth > 7:
            self.borderWidth = 7
        elif self.borderWidth < 1:
            self.borderWidth = 1
        canvas:attrColor(self.borderR, self.borderG, self.borderB, 255)
        for i in range(1, self.borderWidth + 1):
            canvas:drawRect('frame', self.x + (i - 1), self.y + (i - 1), self.width + (-i + 1), self.height + (-i + 1))
