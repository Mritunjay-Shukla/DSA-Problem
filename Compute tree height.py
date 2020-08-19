class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
def maxDepth(node):
    if node is None:
        return 0 ;
    else :
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)
            
        if (lDepth > rDepth):
            return lDepth+1
        else:
            return rDepth+1
