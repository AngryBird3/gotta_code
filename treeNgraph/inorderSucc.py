'''
Created on Dec 22, 2012

@author: dharadarji
Given: Graph, with each node has a link to parent
Goal: Find in-order successor of a node

worst case O(height of the tree) - right leaf node - deepest
'''

class graph:
    def __init__(self, data, left, right, parent):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        
'''        
 Constructed binary tree is
             1
           /   \
         2      3
       /  \    /
     4     5  6
    /
   7
in-order traversal: 7 4 2 5 1 6 3
'''
node1 = graph(1, None, None, None)
node2 = graph(2, None, None, node1)
node3 = graph(3, None, None, node1)
node4 = graph(4, None, None, node2)

node7 = graph(7, None, None, node4)
node4 = graph(4, node7, None, node2)
node5 = graph(5, None, None, node2)
node2 = graph(2, node4, node5, node1)
node6 = graph(6, None, None, node3)
node3 = graph(3, node6, None, node1)
node1 = graph(1, node2, node3, None)

def leftMostChild(n):
    if n == None:
        return None
    while n.left != None:
        n = n.left
    return n.data

def inorderSucc(e):
    if e != None:
        #check if it has left child, yes or root node: find leftmost of its right
        if e.left != None or e.parent == None:
            return leftMostChild(e.right)
        #here because, e is right child, go up until we are on left
        p=e.parent
        while p != None:
            if p.left == e:
                break
            e = p
            p = e.parent
        return p.data
    
print inorderSucc(node2)


