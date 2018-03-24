'''
Created on Dec 22, 2012

@author: dharadarji
Given: Two very large binary tree T1 and T2, T1 millions nodes, T2 hundreds nodes
Goal: T2 is subtree of T1?
'''

class tree:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        
'''        
 Constructed binary tree T1 is
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
Constructed binary tree T2 is
    2
   / \
  4   5 
'''
t2node4 = tree(4, None, None)
t2node5 = tree(5, None, None)
t2node2 = tree(2, node4, node5)

def containsTree(t1, t2):
    #empty tree is always subtree 
    if t2 == None:
        return True
    else:
        return subtree(t1, t2)
    
def subtree(t1, t2):
    #big t1 is empty
    if t1 == None:
        return False
    if t1.data == t2.data:
        return matchTree(t1, t2)
    else:
        return subtree(t1.left, t2) or subtree(t1.right, t2)
    
def matchTree(t1, t2):
    #nothing left in subtree
    if t1 == None and t2 == None:
        return True
    #big tree empty and subtree still not found
    if t1 == None or t2 == None:
        return False
    #data doesn't match
    if t1.data != t2.data:
        return False
    return (matchTree(t1.left, t2.left) and matchTree(t1.right, t2.right))
        
print containsTree(node1, t2node2)