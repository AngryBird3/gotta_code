'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, l, r):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    # @param {TreeNode} root
    # @return {boolean}
    def isSymmetric(self, root):
		l = dict()
		l[0] = [root]
		levels = [0]
		for level in levels:
			for node in l[level]:
				if node.left or node.right:
					levels.append(level+1)
					if (level+1) not in l:
						l[level + 1] = list()
					if node.left:
						l[level + 1].append(node.left)
					else:
						dummy = TreeNode("#", None, None)
						l[level + 1].append(dummy)
					if node.right:
						l[level + 1].append(node.right)
					else:
						dummy = TreeNode("#", None, None)
						l[level + 1].append(dummy)
		

		# Now go through level list
		for level in l:
			lnum = len(l[level])
			print "Level: ", level
			for i in range(lnum):
				print l[level][i].val 
				if(l[level][i].val != l[level][lnum - i - 1].val):
					return False
		return True

s = Solution()
'''
n3r = TreeNode(3, None, None)
n3l = TreeNode(2, None, None)
n2r = TreeNode(2, None, n3r)
n2l = TreeNode(2, None, n3l)
n1 = TreeNode(1, n2l, n2r)
'''
#2,3,3,4,null,null,4,null,5,5,null,null,6,6,null,7,8,8,7,9,0,0,1,1,0,0,9
print s.isSymmetric(n1)

