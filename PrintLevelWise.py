def printLevelWiseTree(tree):
    q = [tree]
    while q:
        parent = q.pop(0)
        print(parent.data,':',",".join(str(num) for num in parent.children),sep='')
        for child in parent.children:
            q.append(child)
                  