class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def containsX(tree, x):
    if tree==None:
        return False
    if tree.data==x:
        return True
    for child in tree.children:
        if containsX(child, x):
            return True
    return False               
