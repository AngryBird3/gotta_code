'''
Given a binary tree, find the lowest common ancestor of two given nodes in the tree.
'''
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None 
		self.right = None

class Solution(object):
	def shortest_dist(self, root, p, q, level = 1):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		'''
		Algorithm:
		--------
		dist(root, p) + dist(root, q) - 2 * dist(root, lca)
		Keep track of level from root to current node.
		'''

		if not root:
			return (None, -1)
		if root == p:
			return (root, level)
		if root == q:
			return (root, level)

		matching_left, dp = self.shortest_dist(root.left, p, q, level+1)
		matching_right, dq = self.shortest_dist(root.right, p, q, level+1)

		#If both match, root is LCA
		if matching_left and matching_right:
			dist = dp + dq - 2*level #root is lca
			return (root, dist)

		#Found both the node on one side
		return (matching_left, dp) if matching_left else (matching_right, dq)
t1 = TreeNode(1); t2 = TreeNode(2); t3 = TreeNode(3)
t4 = TreeNode(4); t5 = TreeNode(5); t6 = TreeNode(6)
t7 = TreeNode(7); t8 = TreeNode(8)

t1.left = t2; t1.right = t3
t2.left = t4; t2.right = t5
t5.left = t6; t5.right = t7
t7.right = t8

sol = Solution()
lca, dist= sol.shortest_dist(t1, t4, t8)
if lca:
	print lca.val
	print dist
