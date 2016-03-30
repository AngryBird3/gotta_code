class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
	def rangeBitwiseAnd(self, m, n):
		c = 0
		while(m != n):
			m >>= 1
			n >>= 1
			c += 1
		return m<<c

s = Solution()
print s.rangeBitwiseAnd(5, 7)
