'''
Created on Dec 21, 2012

@author: dharadarji

Algorithm
if |MaxHieght(root) - MinHieght(root)| <=1:
   return true
else:
   return false
   
TODO time complexity O(n)
'''
class tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
'''        
 Constructed binary tree is
             1
           /   \
         2      3
       /  \    /
     4     5  6
    /
   7
'''
node7 = tree(7, None, None)
node4 = tree(4, node7, None)
node5 = tree(5, None, None)
node2 = tree(2, node4, node5)
node6 = tree(6, None, None)
node3 = tree(3, node6, None)
node1 = tree(1, node2, node3)

'''        
 Constructed binary tree is
             1
           /   \
         2      3
       /  \    / \
     4     5  6   8
    /
   7
'''
node27 = tree(7, None, None)
node24 = tree(4, node27, None)
node25 = tree(5, None, None)
node22 = tree(2, node24, node25)
node26 = tree(6, None, None)
node28 = tree(8, None, None)
node23 = tree(3, node26, node28)
node21 = tree(1, node22, node23)

def maxHeight(root):
    if root == None:
        return 0
    else:
        return 1 + max(maxHeight(root.getLeft()), maxHeight(root.getRight()))    
    
def minHeight(root):
    if root == None:
        return 0
    else:
        return 1 + min(minHeight(root.getLeft()), minHeight(root.getRight()))   
    
def isBalanced(root):
    return abs(maxHeight(root) - minHeight(root)) <= 1

print isBalanced(node1)    
print isBalanced(node21)   
     
