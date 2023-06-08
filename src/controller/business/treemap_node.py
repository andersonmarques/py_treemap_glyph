class Treemap_Node:
    def __init__(self):
        self.parent = None
        self.children = []

    def hasChildren(self):
        return len(self.children) > 0

    def getType(self):
        return 'TreemapNode'


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
