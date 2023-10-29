class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def replacewithDepth(tree,d=0):
    if tree is None:
        return
    tree.data = d 
    for child in tree.children:
        replacewithDepth(child,d+1)    
