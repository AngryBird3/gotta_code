'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
'''
class Solution(object):
	"""
	:type n: int
	:rtype: int
	"""
	def climbStairs(self, n):
		if n < 1:
			return 0
		opt = [0 for i in range(n+1)]

		opt[0] = 1
		for i in range(1, n+1):
			if i != 1:
				opt[i] = opt[i-1] + opt[i-2]
			else:
				opt[i] = opt[i-1]

		return opt[i]

	def climbStairs2(self, n):
		if n < 4:
			return n
		x1 = 2
		x2 = 3
		for i in range(n-3):
			x3 = x1 + x2
			x1 = x2
			x2 = x3
		return x3

s = Solution()
print s.climbStairs2(3)
