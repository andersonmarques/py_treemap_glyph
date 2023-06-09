from treemap_node import Treemap_Node
from dimension import Dimension

class Treemap_Level(Treemap_Node):
    def __init__(self, label='', value=0.0, parent=None):
        super().__init__(label, value, parent)
        self.label = label
        self.items = []
        self.value = value # sum of all children values

    def calculate_level_value(self, total_value):
        '''Calculate the value of the level and its children'''
        if self.hasChildren():
            # calculate the value of the children
            for child in self.items:
                child.calculate(total_value)
                self.value += child.value
        else:
            # calculate the value of the level
            self.value = total_value


    def addChild(self, child):
        '''Add a child to the level. The child is a Treemap_Item object'''
        self.items.append(child)

    def draw(self, dimension: Dimension, painter, color):
        '''Draw the level and its children'''
        if self.hasChildren():
            # draw the children
            for child in self.items:
                child.draw(dimension, painter, color)
        else:
            # draw the level
            painter.setBrush(color)
            painter.drawRect(dimension.x, dimension.y, dimension.width, dimension.height)
            painter.drawText(dimension.x, dimension.y, dimension.width, dimension.height, self.label)

    @property
    def items (self):
        return self.__items
    
    @items.setter
    def items(self, items):
        if items == None:
            raise ValueError('Items must not be None')
        self.__items = items

    