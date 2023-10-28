class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

def leafNodeCount(tree):
    if tree == None:
        return 0 
    
    if not tree.children:
        return 1
    count = 0    
    for child in tree.children:
        count= count+leafNodeCount(child)
    return count            
