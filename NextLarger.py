class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(tree, n):
    if tree is None:
        return tree
    nextLarger = None
    if tree.data>n:
        nextLarger= tree
    for child in tree.children:
        temp = nextLargest(child,n)
        if nextLarger is None:
            nextLarger = temp
        elif temp!=None and temp.data<nextLarger.data:
            nextLarger = temp
    return nextLarger                      
