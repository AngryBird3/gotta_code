'''
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
https://www.youtube.com/watch?v=YDf982Lb84o
'''
class Solution(object):
    def numTrees(self, n):
		"""
		:type n: int
		:rtype: int
		"""

		# Enumerate through each #, we can keep each of them as root
		# of course when i is root, 0..i-1 on left and i+1 .. n of right
		# Hence its going to be cartesian product of left ( as uniq BST
		# on left side and uniq BST on right side, "combine left each
		# with righ each" hence cartesian product)

		#Inner loop is clculating for every n = i, what would be
		#Total number of trees.
		#So j will take root as 1 to i
		#opt[i] = # of uniq BST
		if n <= 1:
			return 1
		opt = [0 for i in range(n+1)]	
		opt[0] = opt[1] = 1
	
		for i in range(2, n+1):
			if i == 4:
				print "i: ", i
			for j in range(1, i+1):
				if i == 4:
					print "j-1: ", j-1, " i-j: ", i-j, " opt[i]: ", opt[i]
				opt[i] += opt[j-1] * opt[i-j]

		return opt[i]	

s = Solution()
print s.numTrees(7)
