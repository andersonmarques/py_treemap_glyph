from treemap_level import Treemap_Level
from treemap_item import Treemap_Item

class Treemap:
    def __init__(self):
        self.root = None
    
    def addLevel(self, label: str, value: float):
        '''Add a level to the treemap. The level is a Treemap_Level object'''
        level = Treemap_Level(label)
        if self.root is None:
            self.root = level #root is the first level, so it has no parent. It is a Treemap_Level object
        else:
            self.root.addChild(level) #add a child to the root, which is a Treemap_Level object
            level.parent = self.root #set the parent of the level, which is a Treemap_Level object
        
        level.value = value

    def addItem(self, label: str, value: float, parent):
        item = Treemap_Item(label, value) #create a Treemap_Item object
        item.value = value #set the value of the item
        if parent is not None:
            item.parent = parent #set the parent of the item, which is a Treemap_Level object
            parent.addChild(item) #add the item to the parent, which is a Treemap_Level object

    def create_tree(self, data):
        '''
        Cria uma árvore a partir dos dados. Os dados são uma lista de listas. 
        A primeira lista são os rótulos para os níveis. As outras listas são os itens. 
        O primeiro elemento em cada lista é o rótulo para o item. Os outros elementos são os valores para os níveis.
        '''
        #create the levels
        for i in range(len(data[0])):
            self.addLevel(data[0][i], i)

        #create the items
        for i in range(1, len(data)):
            parent = self.root
            for j in range(len(data[i])):
                self.addItem(data[i][0], data[i][j], parent)
                parent = parent.children[-1]

    def build(self):
        '''This method is called after all the levels and items have been added to the treemap. 
        It calculates the size and position of each item. '''

        # self.root.calculate()
        # self.root.layout()
        pass

    def draw(self, painter, color):
        pass

    