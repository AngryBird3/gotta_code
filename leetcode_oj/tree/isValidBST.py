'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

Hide Company Tags Amazon Microsoft Bloomberg Facebook
Hide Tags Tree Depth-first Search
Hide Similar Problems (M) Binary Tree Inorder Traversal

Difficulty: Medium
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root, smallest=float('-inf'), largest=float('inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        '''
        Algorithm:
            Can't apply BST algorithm here like check root.val > root.left and root.val < root.right
            cause it depends on the ALL root in sequence
            So.. 
            Left side can't be GREATER THAN <LargestValue> and right side can't be LESSTHAN  <SmallestValue>
            for left side: new largest value would be root
            for right-side: new smallest value would be root
            
            Two param: all nodes in that subtree should be larger than smallest
            and smaller than largest
        '''
        if not root:
            return True
        if root.val <= smallest or root.val >= largest:
            return False
        return self.isValidBST(root.left, smallest, root.val) and self.isValidBST(root.right, root.val, largest)
