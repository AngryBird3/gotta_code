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
		* Lets try the top-down approach where we traverse the nodes 
		from the top to the bottom. 
		* First, if the current node is one of the two nodes, it must 
		  be the LCA of the two nodes. 
		* If not, we count the number of nodes that matches either p 
		  or q in the left subtree (which we call totalMatches). 
		* If totalMatches equals 1, then we know the right subtree will 
		  contain the other node. Therefore, the current node must be 
		  the LCA. 
		* If totalMatches equals 2, we know that both nodes are contained
		  in the left subtree, so we traverse to its left child. 
		* Similar with the case where totalMatches equals 0 where we 
		  traverse to its right child.


		Time complexity: worst case O(n^2) - not balanced
		For balanced: O(n)
		http://articles.leetcode.com/lowest-common-ancestor-of-a-binary-tree-part-i
		'''	

		if not root or not p or not q:
			return None
		if root == p or root == q:
			return root

		total_matches = self.count_matching_p_q(root.left, p, q)
		if total_matches == 1:
			return root
		if total_matches == 2:
			return self.lowestCommonAncestor(root.left, p, q)
		else:
			return self.lowestCommonAncestor(root.right, p, q)

	def count_matching_p_q(self, root, p, q):
		if not root:
			return 0
		match = self.count_matching_p_q(root.left, p, q) +\
				self.count_matching_p_q(root.right, p, q)	
		if p == root or q == root:
			return match + 1
		else:
			return match

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
