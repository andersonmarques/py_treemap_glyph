from treemap_node import Treemap_Node
from dimension import Dimension
from typing import List

class Treemap_Level(Treemap_Node):
    def __init__(self, label='', value=0.0, parent=None):
        super().__init__(label, value, parent)

    def addChild(self, child_node: Treemap_Node):
        '''Add a child to the level. The child is a Treemap_Item object'''
        self.children.append(child_node)

    def calculate_value(self) -> float:
        '''Calculate the value of the item'''
        if self.hasChildren():
            # calculate the value of the children
            for child in self.children:              
                self.value += child.calculate()
            return self.value
        else:
            # calculate the value of the level
            return self.value

    def draw(self, dimension: Dimension, painter, color):
        '''Draw the level and its children'''
        if self.hasChildren():
            # draw the children
            for child in self.children:
                child.draw(dimension, painter, color)
        else:
            # draw the level
            painter.setBrush(color)
            painter.drawRect(dimension.x, dimension.y, dimension.width, dimension.height)
            painter.drawText(dimension.x, dimension.y, dimension.width, dimension.height, self.label)

    


    