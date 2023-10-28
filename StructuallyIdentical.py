def isIdentical(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if tree1.data!=tree2.data:
        return False
    if len(tree1.children)!=len(tree2.children):
        return False    
    for i in range(len(tree1.children)):
        if not isIdentical(tree1.children[i], tree2.children[i]):
            return False
    return True            
