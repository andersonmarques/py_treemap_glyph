from treemap_node import Treemap_Node
from dimension import Dimension

class Treemap_Item(Treemap_Node):

    def __init__(self, label, value, parent=None):
        super().__init__(label, value, parent)
        self.label = label
        self.value = 0.0
        self.parent = None    

    def addChild(self, child):
        raise NotImplementedError("Treemap_Item does not support adding children")
    
    def draw(self, dimension, painter, color):
        '''Draw the item'''
        # draw the item
        painter.setBrush(color)
        painter.drawRect(dimension.x, dimension.y, dimension.width, dimension.height)
        painter.drawText(dimension.x, dimension.y, dimension.width, dimension.height, self.label)
