'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.

Hide Company Tags Microsoft
Hide Tags Tree Depth-first Search
Hide Similar Problems (E) Path Sum (M) Sum Root to Leaf Numbers
Difficulty: Hard
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = -sys.maxint
        self.helper(root)
        return self.maxSum
        
    def helper(self, node):
        if not node:
            return 0
        #bottom up
        left = max(0, self.helper(node.left))
        right = max(0, self.helper(node.right))
        self.maxSum = max(self.maxSum, left + right + node.val)
        return max(left, right) + node.val #why not thisleft + right + node.val - notes
