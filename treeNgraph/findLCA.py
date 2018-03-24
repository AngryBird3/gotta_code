'''
Created on Dec 22, 2012

@author: dharadarji

1) Given: Binary tree, (no parent link)
Goal: Find first common ancestor of 2 nodes in binary tree
TODO O ??

2) Given: Binary tree WITH parent link
Goal: same

Algo: Follow parent link of p and q, make it visited, 
if following parent , you encounter parent is visited,
return that

3) Given: BST
Goal: same

Algo:

'''
class tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
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

def findLCA(root, p, q):
    if root == None or p == None or q == None:
        return None
    
    if root == p or root == q:
        return root
    
    #get LCA of p and q in left subtree
    l = findLCA(root.left, p, q)
    r = findLCA(root.right, p, q)
    if l != None and r != None:
        return root
    elif l != None:
        return l
    else:
        return r
    
node = findLCA(node1, node6, node3)
print node.data
    