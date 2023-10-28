def sumOfAllNodes(root) :
    if root == None:
        return 0 
    sum = root.data
    for child in root.children:
        sum = sum+ sumOfAllNodes(child)
    return sum  