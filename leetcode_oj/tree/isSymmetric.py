'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

Hide Company Tags LinkedIn Bloomberg Microsoft
Hide Tags Tree Depth-first Search Breadth-first Search
Difficulty: Easy
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
    def isSymmetric(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)
        
    def helper(self, left, right):
        if not left and not right:
            return True
        if not left and right:            
            return False
        if not right and left:            
            return False
                
        return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)


