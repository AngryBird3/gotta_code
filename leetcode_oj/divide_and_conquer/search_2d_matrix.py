'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''
class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
	def searchMatrix(self, matrix, target):
		if not matrix:
			return False
		if len(matrix[0]) != 0 :
			return self.helper(matrix, target)
		else:
			return False

	def helper(self, m, target):
		# Start at upper right corner
		i = 0
		j = len(m[0]) - 1
		
		while (i <= len(m)-1) and (j >= 0):
			if m[i][j] == target:
				return True
			elif m[i][j] < target:
				i += 1
			else:
				j -= 1	
		return False

s = Solution()
m = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
m1 = [[-5]]
print s.searchMatrix(m1, -5)
