'''
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

Hide Company Tags Pocket Gems Microsoft Facebook
Hide Tags Tree
Hide Similar Problems (M) Binary Tree Inorder Traversal (M) Binary Search Tree Iterator
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        if not p:
            return None
        
        #if p has right nodes, find left most of rightside
        if p.right:
            return self.leftMost(p.right)
        
        #We need to search for its parent
        #starting from root
        succ = None
        while root:
            #If cur node is succ
            '''
            Don't do this: what if the root node is succ, i.e. [3,1,4,null,2]
            if root.left:
                if root.left.val == p.val:
                    return root
            '''
                    
            if p.val < root.val:
                succ = root
                root = root.left
            elif p.val > root.val:
                root = root.right
            else:
                break
        return succ
                
    def leftMost(self, root):
        while root.left:
            root = root.left
        return root
