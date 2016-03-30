'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''
class Solution(object):
	def numSquares(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		# Least # of squares which sum to i
		opt = [float('inf')] * (n+1)
		opt[0] = 0
		for i in range(1, n+1):
			j = 1
			while j*j <= i:
				print " i: ", i, " j: ", j, " i-j*j: ", i-j*j, " opt[i-j*j]: ", opt[i - j*j]
				# for each i, it must be sum of some#(i - j*j) and a perfect square j*j
				opt[i] = min(opt[i], opt[i - j*j]+1)
				j += 1
		return opt[-1]

	def bfs_numSquares(self, n):
		'''
		Imagine that you have a graph where vertices are numbers from 0 to n. 2 vertices are connected dirrectly if their values are different by a square number. for example: 1 and 2 connected, 2 and 3 connected, 2 and 6 connected, 2 and 11 connected, 1 and 5 connected, 1 and 10 connected, etc.
		'''
		from collections import deque
		q = deque([(0, 0)])
		visited = set()
		while q:
			i, step = q.popleft()
			step += 1
			for j in xrange(1, n+1):
				k = i + j*j
				if k == n:
					return step
				if k > n:
					break
				if k not in visited:
					visited.add(k)
					q.append((k, step))

s = Solution()
print s.numSquares(1)
