from treemap_node import Treemap_Node

class Treemap_Item(Treemap_Node):
    def __init__(self, label, value):
        super().__init__()
        self.label = label
        self.value = value

    def getType(self):
        return 'TreemapItem'


# from hashMap import HashMap
# from treemap_node import TreemapNode

# class TreemapItem(TreemapNode):
#     def __init__(self, o=None):
#         super().__init__(o)
#         self.visible = True
#         self.useLabel = False
#         self.columnLabel = ''
#         self.labelFamily = 'vera'
#         self.labelSize = 15
#         self.labelMode = 'italic'
#         self.noCarrinho = False
#         self.map = HashMap()

#     def setValue(self, colunaTamanho):
#         self.valor = self.map.get(colunaTamanho)

#     def setLabel(self, columnName):
#         self.columnLabel = str(columnName)

#     def draw(self):
#         if self.visible:
#             self.setColor()
#             self.drawRectangle()
#             if self.useLabel:
#                 self.configureLabel(str(self.map.get(self.columnLabel)))

#     def setColor(self, r=None, g=None, b=None, a=None):
#         if not self.noCarrinho:
#             self.r = r or 11
#             self.g = g or 126
#             self.b = b or 11
#             self.a = a or 255
#         else:
#             self.r = r or 127
#             self.g = g or 225
#             self.b = b or 127
#             self.a = a or 255

#     def configureLabel(self, label):
#         lwidth, lheight = canvas.measureText(label)
#         if main2.colunaRotulo == 'Preco(R$)':
#             lwidth, lheight = canvas.measureText('R$' + label)
#         if lwidth >= self.width:
#             lwidth, self.labelSize = self.verifyFontCanvasSize(
#                 label, lwidth, self.width, self.labelFamily, self.labelSize, self.labelMode
#             )
#         canvas.attrFont(self.labelFamily, self.labelSize, self.labelMode)
#         xt = (self.width / 2 + self.x) - (lwidth / 2)
#         yt = (self.height / 2 + self.y) - (lheight / 2)
#         if main2.colunaRotulo == 'Preco(R$)':
#             canvas.drawText(xt, yt, 'R$' + label)
#         else:
#             canvas.drawText(xt, yt, label)
#         self.labelSize = 15

#     def setNoCarrinho(self, noCarrinho):
#         self.noCarrinho = noCarrinho

#     def isNoCarrinho(self):
#         return self.noCarrinho

#     def getType(self):
#         return 'TreemapItem'

#     def toString(self):
#         return (
#             ' width: '
#             + str(self.width)
#             + ' height: '
#             + str(self.height)
#             + ' visible: '
#             + str(self.visible)
#             + ' map: '
#             + self.map.toString()
#         )
