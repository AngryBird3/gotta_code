#!/usr/bin/python
'''
Find the least common ancestor in binary tree
'''

class TreeNode:
	def __init__(self, val, l = None, r = None):
		self.val = val
		self.l = l
		self.r = r

class Solution:
	def findAncestor(self, tree, node1, node2):
		if not node1 or not node2:
			return None

		node1_path = list()
		node2_path = list()
		if not self.find_path(tree, node1, node1_path) or \
				not self.find_path(tree, node2, node2_path):
			return None

		print node1_path
		print node2_path

		#Find the first index where path doesn't match
		i = 0
		while (i < len(node1_path) and i < len(node2_path)):
			if node1_path[i] != node2_path[i]:
				break
			i += 1
		return node1_path[i-1]

	def find_path(self, t, n, path):
		if not t:
			return False

		path.append(t.val)

		if n == t.val:
			return True

		if (t.l and self.find_path(t.l, n, path)) or (t.r and self.find_path(t.r, n, path)):
			return True

		path.pop()
		return False

	def lowestCommonAncestor(self, root, p, q):
		if not root:
			return None
		if root == p or root == q:
			return root

		matching_left = self.lowestCommonAncestor(root.l, p, q)
		matching_right = self.lowestCommonAncestor(root.r, p, q)

		print "root : ", root.val, " m_l: ", matching_left.val if matching_left else "None", \
		" m_r: ", matching_right.val if matching_right else "None"

		#If both match, root is LCA
		if matching_left and matching_right:
		    return root

		#Found both the node on one side
		return matching_left if matching_left else matching_right

s = Solution()

t8 = TreeNode(8, None, None)
t0 = TreeNode(0, None, None)
t1 = TreeNode(1, t0, t8)

t4 = TreeNode(4, None, None)
t7 = TreeNode(7, None, None)
t2 = TreeNode(2, t7, t4)
t6 = TreeNode(6, None, None)
t5 = TreeNode(5, t6, t2)
root = TreeNode(3, t5, t1)

print s.lowestCommonAncestor(root, t6, t4)
