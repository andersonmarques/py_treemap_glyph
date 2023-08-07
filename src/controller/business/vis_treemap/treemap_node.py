import abc
from dimension import Dimension

class Treemap_Node (abc.ABC):
    def __init__(self, label, value, parent=None):
        self.__label = label # label of the item
        self._value: float = value # sum of all children values
        self.children = [] # children of the item
        self.parent = parent # parent of the item
        self.dimension = Dimension(0, 0, 0, 0) # dimension of the item

    @abc.abstractmethod
    def calculate_value(self) -> float:
        '''Calculate the value of the item'''
        pass

    @abc.abstractmethod
    def addChild(self, child):
        pass

    @abc.abstractmethod
    def draw(self, dimension: Dimension, painter, color):
        pass

    def hasChildren(self):
        '''Returns True if the node has children, False otherwise'''
        return len(self.children) > 0

    @property
    def dimension(self):
        return self.__dimension
    
    @dimension.setter
    def dimension(self, dimension):
        self.__dimension = dimension

    @property
    def label (self):
        return self.__label
    
    @label.setter
    def label(self, label):
        if label == '':
            raise ValueError('Label must not be empty')
        
        self.__label = label

    
    @property
    def value(self) -> float:
        return self._value
    
    @value.setter
    def value(self, value: float):
        if value < 0: #The treemap can't have negative values
            raise ValueError('Value must be greater than 0')
        self._value = value

# from navigable import Navigable

# class TreemapNode(Navigable):
#     def __init__(self, o=None):
#         super().__init__(o)
#         self.label = ''
#         self.valor = 1

#     def getType(self):
#         return 'TreemapNode'

#     def hasChildren(self):
#         return len(self.children) > 0

#     def getValor(self):
#         return self.valor

#     def organize(self):
#         if self.hasChildren():
#             for child in self.children:
#                 child.organize()
#             self.quickSort(self.children, 0, len(self.children) - 1)
#         return self.children

#     def verifyFontCanvasSize(self, label, labelWidth, nodeWidth, fontFamily, fontSize, fontStyle):
#         aux = labelWidth
#         while labelWidth >= nodeWidth - 2:
#             fontSize -= 1
#             canvas.attrFont(fontFamily, fontSize, fontStyle)
#             labelWidth = canvas.measureText(label)
#         return labelWidth, fontSize

#     def setValue(self, colunaTamanho):
#         pass

#     def quickSort(self, v, low, high):
#         if low < high:
#             pivot = self.partition(v, low, high)
#             self.quickSort(v, low, pivot - 1)
#             self.quickSort(v, pivot + 1, high)

#     def partition(self, v, low, high):
#         pivot = v[high].getValor()
#         i = low - 1
#         for j in range(low, high):
#             if float(v[j].getValor()) >= float(pivot):
#                 i += 1
#                 v[i], v[j] = v[j], v[i]
#         v[i + 1], v[high] = v[high], v[i + 1]
#         return i + 1
