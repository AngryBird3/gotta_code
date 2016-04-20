'''
Given a binary tree, find the lowest common ancestor of two given nodes in the tree.
'''
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None 
		self.right = None

class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		"""
		:type root: TreeNode
		:type p: TreeNode
		:type q: TreeNode
		:rtype: TreeNode
		"""
		'''
		Algorithm:
		--------
		* Like the count_matching_p_q method, we'll go for
		 bottom-up approach
		* We traverse from the bottom, and once we reach a node 
		  which matches one of the two nodes, we pass it up to 
		  its parent.
		* The parent would then test its left and right subtree 
		  if each contain one of the two nodes. 
		* If yes, then the parent must be the LCA and we pass its 
		  parent up to the root.
		* If not, we pass the lower node which contains either one 
		  of the two nodes (if the left or right subtree contains 
		  either p or q), or NULL (if both the left and right subtree
		  does not contain either p or q) up.
		'''

		if not root:
			return None
		if root == p or root == q:
			return root

		matching_left = self.lowestCommonAncestor(root.left, p, q)
		matching_right = self.lowestCommonAncestor(root.right, p, q)

		#If both match, root is LCA
		if matching_left and matching_right:
			return root

		#Found both the node on one side
		return matching_left if matching_left else matching_right
t1 = TreeNode(1); t2 = TreeNode(2); t3 = TreeNode(3)
t4 = TreeNode(4); t5 = TreeNode(5); t6 = TreeNode(6)
t7 = TreeNode(7); t8 = TreeNode(8)

t1.left = t2; t1.right = t3
t2.left = t4; t2.right = t5
t5.left = t6; t5.right = t7
t7.right = t8

sol = Solution()
lca= sol.lowestCommonAncestor(t1, t4, t8)
if lca:
	print lca.val
