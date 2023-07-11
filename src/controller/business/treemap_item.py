from treemap_node import Treemap_Node
from dimension import Dimension

class Treemap_Item(Treemap_Node):

    def __init__(self, label, value, parent=None):
        super().__init__(label, value, parent)
        self.__parent = None    

    def addChild(self, child: Treemap_Node):
        raise NotImplementedError("Treemap_Item does not support adding children")
    
    def calculate_value(self) -> float:
        '''Calculate the value of the item'''
        return self.value
    
    def draw(self, dimension, painter, color):
        '''Draw the item'''
        # draw the item
        painter.setBrush(color)
        painter.drawRect(dimension.x, dimension.y, dimension.width, dimension.height)
        painter.drawText(dimension.x, dimension.y, dimension.width, dimension.height, self.label)

    @property
    def parent(self):
        return self.__parent
    
    @parent.setter
    def parent(self, parent):
        self.__parent = parent
