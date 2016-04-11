'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
'''
class Solution(object):
	def minimumTotal(self, triangle):
		"""
		:type triangle: List[List[int]]
		:rtype: int
		"""

		'''
		Algorithm:
		- "At each step you may move to adjacent numbers on the row below"
		- Of course with 2D OPT[n][i]: will be and nth row and ith column
		  Total. Hence answer would be min(opt[n]) <- last row minimum
		- We can take advantage of "adjacent numbers"
		- Store minimumTotal till now, index of current row used to get
		  minimum
		- opt[n, i] = (min_sum, index) -> and nth row minimum path total
		  and current row's ith column is getting used in my path Total
		- This wont work: [[-1], [2, 3], [1, -1, -3]]
		'''

		if not triangle:
			return 0
		opt = [None] * len(triangle) 
		opt[0] = [triangle[0][0]]

		for i in range(1, len(triangle)):
			opt[i] = [float('inf')] * len(triangle[i])
			for j in range(0, len(triangle[i])):
				if j < (len(triangle[i-1])):
					opt[i][j] = opt[i-1][j] + triangle[i][j]
				if j > 0:
					opt[i][j] = min(opt[i][j], \
									opt[i-1][j-1] + triangle[i][j])
			print opt[i]

		return min(opt[-1])

	def minimumTotal2(self, triangle):
		if not triangle:
			return 0
		opt = [None] * len(triangle) 
		opt[0] = triangle[0][0]

		temp = opt[0]
		for i in range(1, len(triangle)):
			for j in range(0, len(triangle[i])):
				#Store current
				temp1 = opt[j]
				if j < (len(triangle[i-1])):
					if opt[j] == None:
						opt[j] = 0
					opt[j] = opt[j] + triangle[i][j]
				if j > 0:
					if opt[j] == None:
						opt[j] = float('inf')
					opt[j] = min(opt[j], temp + triangle[i][j])

				#Restore:
				temp = temp1
			print opt

		return min(opt)
		

s = Solution()
l = [[-1],[2,3],[1,-1,-3]]
l = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
print s.minimumTotal2(l)
