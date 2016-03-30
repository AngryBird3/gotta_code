'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, l, r):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
	def rightSideView(self, root):
		if not root:
			return list()
		nodes_by_level = {0 : [root.val]}
		self.helper(root, nodes_by_level, 1)
		node_on_rightside = list()
		for level in nodes_by_level:
			if nodes_by_level[level]:
				node_on_rightside.append(nodes_by_level[level].pop())
		return node_on_rightside
		
	def helper(self, node, nodes_by_level, level):
		if level not in nodes_by_level:
			nodes_by_level[level] = list()
		if node.left:
			nodes_by_level[level].append(node.left.val)	
			self.helper(node.left, nodes_by_level, level + 1)
		if node.right:
			nodes_by_level[level].append(node.right.val)
			self.helper(node.right, nodes_by_level, level + 1)
		

s = Solution()
n7 = TreeNode(7, None, None)
n4 = TreeNode(4, n7, None)
n5 = TreeNode(5, None, None)
n2 = TreeNode(2, n4, None)
n3 = TreeNode(3, n5, None)
n1 = TreeNode(1, n2, n3)
print s.rightSideView(n1)

