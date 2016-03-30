'''
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
'''

class TreeNode:
	def __init__(self, val,left=None, right=None, parent=None):
		self.val = val
		self.left = left 
		self.right = right
		self.parent = parent
			
class BST:
	def __init__(self, size=0):
		self.root = None
		self.size = size
	
	def insert(self, val, t):
		if self.root:
			ret = self.insert_helper(val, self.root, t)
			return ret
		else:
			self.root = TreeNode(val)
			#if val == t:
			#	return True
		self.size += 1

	def get_size(self):
		return self.size

	def insert_helper(self, val, cur, t):
		if val < cur.val:
			if cur.left:
				return self.insert_helper(val, cur.left, t)
			else:
				cur.left = TreeNode(val, parent=cur)	
				if abs(cur.val - val) <= t:
					return True 
				else:
					return False
		elif val > cur.val:
			if cur.right:
				return self.insert_helper(val, cur.right, t)
			else:
				cur.right = TreeNode(val, parent=cur)
				if abs(cur.val - val) <= t:
					return True 
				else:
					return False
		else:
			#Same
			if abs(val - val) <= t:
				return True
			else:
				return False
	def get_val(self, val, root):
		if self.root:
			return self.get_val_helper(val, root)
		else:
			return None
	
	def get_val_helper(self, val, cur):
		if cur.val == val:
			return cur
		if val < cur.val:
			if cur.left:
				return self.get_val_helper(val, cur.left)
			else:
				return None
		else:
			if cur.right:
				return self.get_val_helper(val, cur.right)
			else:
				return None

	def delete(self, val):
		node = self.get_val(val, self.root)
		if not node:
			raise KeyError('Error, key not in tree')
		else:
			self.delete_helper(node)
		self.size -= 1

	def delete_helper(self, cur):
		#Leaf node
		if not cur.left and not cur.right:
			if not cur.parent:
				self.root = None
			elif cur == cur.parent.left:
				cur.parent.left = None
			else:
				cur.parent.right = None
		#Interior
		elif cur.left and cur.right:
			successor = self.find_min(cur.right)
			cur.val = successor.val 
			self.delete_helper(successor)
		#one node
		else:
			if cur.left:
				# if it has left child and cur is right child of its parent
				if not cur.parent:
					self.root = cur.left
				elif cur == cur.parent.right:
					cur.left.parent = cur.parent
					cur.parent.right = cur.left
				else:
					cur.left.parent = cur.parent
					cur.parent.left = cur.left
			else:
				if not cur.parent:
					self.root = cur.right
				# if it has right child and cur is right child of its parent
				elif cur == cur.parent.right:
					cur.right.parent = cur.parent
					cur.parent.right = cur.right
				else:
					cur.right.parent = cur.parent
					cur.parent.left = cur.right

	def find_min(self, cur):
		while cur.left:
			cur = cur.left
		return cur	

	def print_tree(self):
		level = {0 : [self.root.val]}
		self.print_helper(self.root, level, 1)
		for l in level:
			for node in level[l]:
				print node,
			print "\n"
	
	def print_helper(self, root, level, l):
		if root.left:
			if l not in level:
				level[l] = list()
			level[l].append(root.left.val)
			self.print_helper(root.left, level, l+1)	
		if root.right:
			if l not in level:
				level[l] = list()
			level[l].append(root.right.val)
			self.print_helper(root.right, level, l+1)	
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
	def containsNearbyAlmostDuplicate(self, nums, k, t):
		b = BST()
		i = 0
		#for i in range(0, min(k+1, len(nums))):
		while True:
			ret = b.insert(nums[i], t)
			if ret:
				return True
			i += 1
			if i > k or i == len(nums):
				if k == 0 :
					return False
				break
		b.print_tree()
		for i in range(k+1, len(nums)):
			b.delete(nums[i-k-1])
			print "---------- After deleting ", nums[i-k-1], " ------------"
			b.print_tree()
			ret = b.insert(nums[i], t)
			print "---------- After inserting ", nums[i], " ------------"
			b.print_tree()
			if ret:
				return True
		return False

s = Solution()
print s.containsNearbyAlmostDuplicate([3, 6, 0, 4], 2, 2)
