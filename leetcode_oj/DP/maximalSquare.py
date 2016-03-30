'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''
class Solution(object):
    def maximalSquare(self, matrix):
		"""
		:type matrix: List[List[str]]
		:rtype: int
		"""
		# opt[i][j] = max length(or height!) of a square ending at [i][j]
		# In order to get opt[i][j], it has to be 1, or else no suare can form
		# so that case 0. 
		# if its one, then MINIMUM of what neighbors got +1 (to increase size of square)
		opt = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]

		maxarea = 0
		for i in range(len(matrix)):
			opt[i][0] = int(matrix[i][0]) 
			maxarea = max(maxarea, opt[i][0])
			print "Maxarea: ", maxarea

		for j in range(len(matrix[0])):
			opt[0][j] = int(matrix[0][j])
			maxarea = max(maxarea, opt[0][j])
			print "Maxarea: ", maxarea

		for i in range(1, len(matrix)):
			for j in range(1, len(matrix[i])):
				if int(matrix[i][j]):
					opt[i][j] = min(opt[i-1][j-1], opt[i-1][j], opt[i][j-1]) + 1
					print "i: ", i, "j: ", j, "opt[i][j]: ", opt[i][j]
					maxarea = max(maxarea, opt[i][j])
					print "Maxarea: ", maxarea, " i: ", i, " j: ", j
		
		return maxarea*maxarea

s = Solution()
a = [[1,0,1,0,0],
	 [1,0,1,1,1],
	 [1,1,1,1,1],
	 [1,0,0,1,0]]
b = [["0", "0"],
	 ["0", "0"]]
print s.maximalSquare(a)
