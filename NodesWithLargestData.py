def maxDataNode(tree):
    if tree == None:
        return None
    maximum = tree.data
    for child in tree.children:
        child_max = maxDataNode(child)
        if child_max is not None:
            maximum = max(maximum,child_max) 
    return maximum       
