'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,20,4,5,2,7],
    _3_
   /   \
  9    20
 / \   / \
4   5 2   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]
'''
import collections
# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def verticalOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		'''
		Algorithm:
			Think like x y cordinate system
			with root as (0)
			left as -1 and right as +1
			Go through all nodes and assign cordinate following same'
			Print from min of coordinate value to max
		'''
		if not root:
			return list()
		h = {}
		self.assign_coordinates(root, h, 0)
		res = list()
		minm = min(h.keys())
		maxm = max(h.keys())
		for i in range(minm, maxm+1):
			res.append(h[i])
		return res

	def assign_coordinates(self, root, h, dist):
		if not root:
			return
		if dist in h:
			h[dist].append(root.val)
		else:
			h[dist] = [root.val]

		self.assign_coordinates(root.left, h, dist - 1)
		self.assign_coordinates(root.right, h, dist + 1)

	def verticalOrder2(self, root):
		if not root:
			return list()

		h = collections.defaultdict(list)
		q = [(root, 0)]

		for node, i in q:
			if node:
				h[i].append(node.val)
				q.append((node.left, i-1))
				q.append((node.right, i+1))
		return [h[i] for i in sorted(h)]
s = Solution()

root = TreeNode(3)
t9 = TreeNode(9)
t20 = TreeNode(20)
t15 = TreeNode(15)
t7 = TreeNode(7)
root.left = t9; root.right = t20
t20.left = t15; t20.right = t7

res = s.verticalOrder2(root)
print res
