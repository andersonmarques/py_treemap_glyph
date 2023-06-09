from treemap_level import Treemap_Level
from treemap_item import Treemap_Item

class Treemap:
    def __init__(self):
        self.root = None

    def addLevel(self, label, value):
        '''Add a level to the treemap. The level is a Treemap_Level object'''
        level = Treemap_Level(label)
        if self.root is None:
            self.root = level #root is the first level, so it has no parent. It is a Treemap_Level object
        else:
            self.root.addChild(level) #add a child to the root, which is a Treemap_Level object
        
        level.value = value

    def addItem(self, label, value, parent):
        item = Treemap_Item(label, value) #create a Treemap_Item object
        parent.addChild(item) #add the item to the parent, which is a Treemap_Level object
        item.value = value #set the value of the item
        item.parent = parent #set the parent of the item, which is a Treemap_Level object

    def build(self):
        '''Build the treemap'''
        # self.root.calculate()
        # self.root.layout()
        pass

    def draw(self, painter, color):
        pass

    