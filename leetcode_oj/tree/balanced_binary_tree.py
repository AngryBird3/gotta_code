'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
Difficulty: Easy
Bloomberg
Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Maximum Depth of Binary Tree

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isBalanced(self, root):
        if not root:
            return True
        else:
            depth_left = self.depth(root.left)
            depth_right = self.depth(root.right)
            if abs(depth_left - depth_right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
    def depth(self, node):
        if not node:
            return 0
        else:
            return 1 + max(self.depth(node.left), self.depth(node.right))

