'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
'''
class Solution(object):
	def spiralOrder(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: List[int]
		"""
		if not matrix:
			return list()
		res = list()
		'''
		While count != n*m:
			# 1) Left to right row
			# 2) Top to bottom column
			# 3) Right to left row
			# 4) Bottom to top col
		'''	
		m = len(matrix)
		n = len(matrix[0])
		count = 0
		start = 0
		end_r = m
		end_c = n
		print "m : ", m , " n: ", n
		while count < (n)*(m):
			#1) Left to right row
			for i in range(start, end_c):
				res.append(matrix[start][i])
				count += 1
			print "After 1): ", res
			if count >= n*m:
				break
			#1) Top to bottom col
			for i in range(start+1, end_r):
				res.append(matrix[i][end_c-1])
				count += 1
			print "After 2): ", res
			if count >= n*m:
				break
			#2) Right to left row
			for i in range(end_c-1-1, start-1, -1):
				res.append(matrix[end_r-1][i])
				count += 1
			print "After 3): ", res
			if count >= n*m:
				break
			#4) Bottom to top col
			for i in range(end_r-1-1, start, -1):
				res.append(matrix[i][start])
				count += 1
			start += 1
			end_c-= 1
			end_r-=1
			print "After 4): ", res
		return res
s = Solution()
'''
m = [
	 [1,2,3],
	 [4,5,6],
	 [7,8,9]
	]
m = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
	 [14,15,16,17]]
'''
m = [[2,3]]
'''
m = [[2],
	 [3],
	 [4]]
m = [[2,5,8],
	 [4,0,-1]]
'''
print s.spiralOrder(m)
