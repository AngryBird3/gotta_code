'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, l, r):
        self.val = x
        self.left = l
        self.right = r

class Solution(object):
	def closestValue(self, root, target, ans=None, val=None):
		"""
		:type root: TreeNode
		:type target: float
		:rtype: int
		"""
		if not root:
			return val
		
		if not ans or ans > abs(target - root.val):
			ans = abs(target - root.val)
			val = root.val
		#Or recurse
		if target < root.val:
			return self.closestValue(root.left, target, ans, val)
		else:
			return self.closestValue(root.right, target, ans, val)

s = Solution()
'''
t7 = TreeNode(7, None, None)
t3 = TreeNode(3, None, t7)
t9 = TreeNode(9, None, None)
t8 = TreeNode(8, t3, t9)

t11 = TreeNode(11, None, None)
t13 = TreeNode(13, t11, None)
t10 = TreeNode(10, t8, t13)

print s.closestValue(t7, 12.5)
'''
t1 = TreeNode(1, None, None)
t3 = TreeNode(3, None, None)
t2 = TreeNode(2, t1, t3)
t5 = TreeNode(5, None, None)
t4 = TreeNode(4, t2, t5)
print s.closestValue(t4, 3.7)
