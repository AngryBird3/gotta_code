'''
Given a binary tree, flatten it to a linked list in-place.
For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
'''
class Node:
    def __init__(self, x, l, r):
        self.val = x
        self.left = l
        self.right = r 

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
	def flatten(self, root):
		temp = root
		l = list() 
		while temp or l:
			if temp.right:
				l.append(temp.right)
			if temp.left:
				temp.right = temp.left
				temp.left = None
			elif(l):
				n = l.pop()
				temp.right = n	
			temp = temp.right
	
def print_tree(node):
	while node:
		if node.left:
			print "ERROR"
			break
		else:
			print node.val
		node = node.right

n6 = Node(6, None, None)
n4 = Node(4, None, None)
n3 = Node(3, None, None)
n5 = Node(5, None, n6)
n2 = Node(2, n3, n4)
n1 = Node(1, n2, n5)

s = Solution()
s.flatten(n1)
print_tree(n1)
