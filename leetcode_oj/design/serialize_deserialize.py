'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''

'''
Algorithm:

Similar to leetcode, Traverse pre-order, adding # for
NULL child
'''
import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
	NULL_VAL = "#"
	SEPARATOR = ","
	def serialize(self, root):
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""
		data = []
		self._helper(root, data)
		data = Codec.SEPARATOR.join(data)
		print data
		return data

	def _helper(self, root, data):
		val = root.val if root else Codec.NULL_VAL
		if root:
			data.append(str(val))
			self._helper(root.left, data)
			self._helper(root.right, data)
		else:
			data.append(str(val))

	def deserialize(self, data):
		"""Decodes your encoded data to tree.

		:type data: str
		:rtype: TreeNode
		"""	
		val = data.split(Codec.SEPARATOR)
		q = collections.deque(val)
		return self._helper_d(q)

	def _helper_d(self, q):
		val = q.popleft()
		if val == Codec.NULL_VAL:
			return None
		node = TreeNode(val)
		#print "node: ", node.val
		#print "left q: ", q
		node.left = self._helper_d(q)
		#print "right q: ", q
		node.right = self._helper_d(q)
		return node
				
def level_order(root):
	if not root:
		return
	q = collections.deque()
	q.append(root)
	while q:
		n = len(q)
		for i in range(n):
			node =  q.popleft()
			print node.val, "	",
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
			
		print ""	
# Your Codec object will be instantiated and called as such:
codec = Codec()
'''
t1 = TreeNode(1); t2 = TreeNode(2); t3 = TreeNode(3)
t4 = TreeNode(4); t5 = TreeNode(5)

t1.left = t2; t1.right = t3
t3.left = t4; t3.right = t5
'''
tn1 = TreeNode(-1); t0 = TreeNode(0); t1 = TreeNode(1)
tn1.left = t0; tn1.right = t1;
new_root = codec.deserialize(codec.serialize(tn1))
level_order(new_root)
