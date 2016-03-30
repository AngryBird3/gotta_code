'''
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    # @param {TreeNode} root
    # @return {integer}
	def sumNumbers(self, root):
		if not root:
			return 0
		root_to_leaf_nums = list()
		self.helper(root, 0, root_to_leaf_nums)
		return sum(root_to_leaf_nums)

	def helper(self, node, num, nums):
		if node.left and node.right:
			self.helper(node.left, num * 10 + node.val, nums)
			self.helper(node.right, num * 10 + node.val, nums)
		elif node.left and not node.right:
			self.helper(node.left, num * 10 + node.val, nums)
		elif node.right and not node.left:
			self.helper(node.right, num * 10 + node.val, nums)
		else:
			nums.append(num * 10 + node.val)
s = Solution()
n4 = TreeNode(4, None, None)
n5 = TreeNode(5, None, None)
n7 = TreeNode(7, None, None)
n2 = TreeNode(2, n4, None)
n3 = TreeNode(3, n5, n7)
n1 = TreeNode(1, n2, n3)
print s.sumNumbers(n3)
