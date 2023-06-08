from treemap_level import TreemapLevel
from treemap_item import Treemap_Item
from squarified_treemap import Squarified_Treemap
from treemap_node import Treemap_Node

class Treemap:
    def __init__(self):
        self.root = Treemap_Node()
        self.squarified_treemap = None

    def setRoot(self, root):
        self.root = root

    def addLevel(self, label, value):
        level = TreemapLevel(label, value)
        self.root.children.append(level)
        level.parent = self.root

    def addItem(self, label, value):
        item = Treemap_Item(label, value)
        self.root.children.append(item)
        item.parent = self.root

    def build(self):
        self.squarified_treemap = Squarified_Treemap(self.root)
        self.squarified_treemap.calculateLayout()

    def draw(self):
        if self.squarified_treemap:
            self.squarified_treemap.draw()


# from treemap_level import TreemapLevel

# class Treemap:
#     def __init__(self):
#         self.dataset = {}
#         self.root = TreemapLevel()
#         self.hierarchy = []
#         self.sizeColumn = ''
#         self.labelColumn = ''
#         self.colorColumn = ''

#     def init(self, dataset, width, height, x=0, y=0):
#         self.dataset = dataset
#         self.root = TreemapLevel()
#         self.root.parent = None
#         self.root.label = 'Celulares'
#         self.root.x = x
#         self.root.y = y
#         self.root.width = width
#         self.root.height = height
#         self.root.resizeBorder()
#         self.squarifier = squarify

#     def setSizeColumn(self, columnName):
#         self.root.setValue(columnName)
#         self.root.organize()

#     def setLabelColumn(self, columnName):
#         self.labelColumn = str(columnName)
#         self.setTreemapItemLabel(self.root.children, True)

#     def setTreemapItemLabel(self, children, isUseLabel):
#         for v in children:
#             if v.getType() == 'TreemapItem':
#                 v.useLabel = isUseLabel
#                 if v.useLabel:
#                     v.setLabel(self.labelColumn)
#             else:
#                 self.setTreemapItemLabel(v.children, isUseLabel)

#     def setColorColumn(self, columnName):
#         pass

#     def setHierarchy(self, hierarchy):
#         self.hierarchy = hierarchy or []
#         for v in self.dataset.getDataset():
#             self.root.insert(self.hierarchy, v)

#     def draw(self):
#         self.squarifier.squarify(self.root)
#         self.root.draw()