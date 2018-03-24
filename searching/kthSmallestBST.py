'''
Created on Jan 30, 2013

@author: dharadarji

Find the kth smallest element in the binary search tree - in O(n lg n)

Algo:
1. k == num_elements(left subtree of T), then the answer we're looking 
   for is the value in node T
2. k > num_elements(left subtree of T) then obviously we can ignore the 
   left subtree, because those elements will also be smaller than the kth 
   smallest. So, we reduce the problem to finding the 
   k - num_elements(left subtree of T) smallest element of the right subtree.
3. k < num_elements(left subtree of T), then the kth smallest is somewhere in
   the left subtree, so we reduce the problem to finding the kth smallest 
   element in the left subtree.
   
or Inorder
'''

class graph:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
"""
def findKthSmallest(root, k):
    print "[DEBUG] I'm at node - ", root.data, "k: ", k
    if root == None or k < 0:
        return
    print "[DEBUG] Calling for left child ..."
    findKthSmallest(root.left, k)
    --k
    if(k == 0):
        print root.data
    print "[DEBUG] Calling for right child ..."
    findKthSmallest(root.right, k)
"""
"""
def num_elements(root):
    if root == None:
        return 0
    return 1 + num_elements(root.left) + num_elements(root.right)

def findKthSmallest(root, k):
    print "[DEBUG]: @ node - ", root.data, "k: ", k
    print "[DEBUG]: num_elements - ", num_elements(root.left)
    if k == num_elements(root.left) + 1:
        print root.data
    elif k > num_elements(root.left):
        return findKthSmallest(root.right, k - num_elements(root.left) - 1)
    else:
        return findKthSmallest(root.left, k)
"""

'''        
 Constructed binary tree is
             12
           /   \
         9      15
       /  \    /  \
     7     10  14  16
    /           \
   6             13
'''
node6 = graph(6, None, None)
node7 = graph(7, node6, None)
node10 = graph(10, None, None)
node9 = graph(9, node7, node10)
node13 = graph(13, None, None)
node14 = graph(14, None, node13)
node16 = graph(16, None, None)
node15 = graph(15, node14, node16)
node12 = graph(12, node9, node15)

#findKthSmallest(node12, 6)    
