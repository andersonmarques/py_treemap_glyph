class Node:
    def __init__(self, o=None):
        self.parent = None
        self.children = []

    def hasChildren(self):
        return len(self.children) > 0
