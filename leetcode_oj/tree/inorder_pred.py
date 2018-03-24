'''
Given a binary search tree and a node in it, find the in-order predecessor of that node in the BST.

Note: If the given node has no in-order predecessor in the tree, return null.

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderPredecessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not p:
            return None
        
        #if p has right nodes, find left most of rightside
        if p.left:
            return self.rightMost(p.left)
        
        #We need to search for its parent
        #starting from root
        pred = None
        while root:
            # I'm changing pred when I move to right side
            # cause that is min element that can come before
            if p.val > root.val:
                pred = root
                root = root.right
            elif p.val < root.val:
                root = root.left
            else:
                break
        return pred
                
    def rightMost(self, root):
        while root.right:
            root = root.right
        return root
