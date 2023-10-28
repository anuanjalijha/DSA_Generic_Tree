
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans

def maxSumNode(tree):
    if not tree:
        return None
    ans, ansSum = tree, tree.sum()
    for child in tree.children:
        temp,tempSum = maxSumNode(child)
        if tempSum>ansSum:
            ans,ansSum = temp,tempSum
    return ans, ansSum            
    #############################
