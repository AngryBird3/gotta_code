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
	
	def insert(self, val):
		if self.root:
			self.insert_helper(val, self.root)
		else:
			self.root = TreeNode(val)
		self.size += 1

	def get_size(self):
		return self.size

	def insert_helper(self, val, cur):
		if val < cur.val:
			if cur.left:
				self.insert_helper(val, cur.left)
			else:
				cur.left = TreeNode(val, parent=cur)	
		else:
			if cur.right:
				self.insert_helper(val, cur.right)
			else:
				cur.right = TreeNode(val, parent=cur)

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
			if cur == cur.parent.left:
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
					self.root = cur
				elif cur == cur.parent.right:
					cur.left.parent = cur.parent
					cur.parent.right = cur.left
				else:
					cur.left.parent = cur.parent
					cur.parent.left = cur.left
			else:
				if not cur.parent:
					self.root = cur
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

	def distance(self, node1, node2):
		if not node1 or not node2:
			return None
		
		node1_path = list()
		node2_path = list()
		if not self.find_path(node1, node1_path) or \
				not self.find_path(node2, node2_path):
			return None

		# Find the first index where path doesn't match
		# That will be the least common ancestor of those
		# two nodes. This is needed to see distance between
		# least common node to node1 + dist(least_common_ancestor,
		# node2)
		i = 0
		while (i < len(node1_path) and i < len(node2_path)):
			if node1_path[i] != node2_path[i]:
				break
			i += 1
		least_common_ancestor_index = i - 1
		node1_index = len(node1_path) - 1
		node2_index = len(node2_path) - 1

		dist = node1_index - least_common_ancestor_index + \
				node2_index - least_common_ancestor_index
		return dist	

	def num_of_hopes(self, root, node1, h=0):
		if not root:
			return float('inf')
		if root.val == node1:
			return h
		if node1 < root.val:
			return self.num_of_hopes(root.left, node1, h+1)
		else:
			return self.num_of_hopes(root.right, node1, h+1)

	def least_common_ancestor(self, root, node1, node2):
		if node1 < root.val and node2 < root.val:
			return self.least_common_ancestor(root.left, node1, node2)
		if node1 > root.val and node2 > root.val:
			return self.least_common_ancestor(root.right, node1, node2)
		return root
		
	def distance2(self, node1, node2):
		#Find the common ancestor
		#Then find num_of_hopes from both the node to common ancestor

		common_ancestor = self.least_common_ancestor(self.root, node1, node2)
		n1 = self.num_of_hopes(common_ancestor, node1)
		n2 = self.num_of_hopes(common_ancestor, node2)
		return n1 + n2
		
b = BST()
l1 = [17, 16, 29, 10, 20, 32, 12, 25, 11]
for n in l1:
	b.insert(n)
print b.distance2(10, 32)
