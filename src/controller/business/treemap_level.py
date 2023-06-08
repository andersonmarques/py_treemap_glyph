from treemap_node import Treemap_Node

class TreemapLevel(Treemap_Node):
    def __init__(self, label, value):
        super().__init__()
        self.label = label
        self.value = value

    def getType(self):
        return 'TreemapLevel'



# from treemap_node import TreemapNode
# from treemap_item import TreemapItem

# class TreemapLevel(TreemapNode):
#     def __init__(self):
#         super().__init__()
#         self.borderWidth = 2
#         self.drawIniY = 20
#         self.font = 'vera'
#         self.fontSize = 15
#         self.fontStyle = 'bold'
#         self.fontColor = 'black'
#         self.ischildrenLeaf = False
#         self.level = 0
#         self.drawableDimension = {}

#     def getType(self):
#         return 'TreemapLevel'

#     def resizeBorder(self):
#         r = Rectangle(width=self.width - (2 * self.borderWidth), height=self.height - self.drawIniY - self.borderWidth,
#                       x=self.x + self.borderWidth, y=self.y + self.drawIniY)
#         self.drawableDimension = r

#     def ischildren(self, treemapItem):
#         b = False
#         if self.ischildrenLeaf:
#             b = self.testFather(treemapItem)
#         return b

#     def insert(self, columnNames, item):
#         if len(columnNames) == 0:
#             self.children.append(item)
#             item.parent = self
#         else:
#             treeLevel = None
#             for v in self.children:
#                 if v.label == item.map.get(columnNames[0]):
#                     treeLevel = v
#                     break

#             if treeLevel is None:
#                 treeLevel = TreemapLevel()
#                 treeLevel.label = item.map.get(columnNames[0])
#                 self.children.append(treeLevel)
#                 treeLevel.parent = self

#             aux = columnNames[1:]
#             treeLevel.insert(aux, item)

#     def draw(self):
#         self.resizeBorder()
#         # self.a = 225
#         Rectangle.draw(self)
#         # canvas:attrColor(self.fontColor)
#         # canvas:drawRect('frame', self.drawableDimension.x, self.drawableDimension.y, self.drawableDimension.width, self.drawableDimension.height)
#         # if self.label ~= '' then
#         #     canvas:attrFont(self.font, self.fontSize, self.fontStyle)
#         #     local lwidth, lheight = canvas:measureText(self.label)
#         #     if lwidth >= self.width then
#         #         lwidth, self.fontSize = self:verifyFontCanvasSize(self.label, lwidth, self.width, self.font, self.fontSize, self.fontStyle)
#         #     end
#         #     canvas:attrFont(self.font, self.fontSize, self.fontStyle)
#         #     local lwidth, lheight = canvas:measureText(self.label)
#         #     local pontoCentralX = (self.width/2)+self.x
#         #     local pontoCentralY = self.y+1
#         #     canvas:drawText(pontoCentralX-(lwidth/2), pontoCentralY, self.label)
#         # end
#         for v in self.children:
#             v.draw()

#     def setValue(self, colunaTamanho):
#         self.valor = 0
#         for v in self.children:
#             v.setValue(colunaTamanho)
#             self.valor = self.valor + v.getValor()

#     def toString(self):
#         string = "[" + self.label + ": "
#         for v in self.children:
#             if v is not None:
#                 string = string + v.toString() + "__\n"
#         string = string + "]"
#         return string