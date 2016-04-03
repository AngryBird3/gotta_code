'''
Implement pow(x, n).
'''
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
	def myPow(self, x, n):
		if n > 0:
			return self.helper(x, n)
		elif n < 0:
			return 1.0/self.helper(x, abs(n))
		else:
			# pow(x, 0) = 1
			return 1

	def helper(self, x, n):
		if n == 1:
			return x
		elif n == 2:
			return x * x
		else:
			#Divide into two parts
			if (n % 2 == 0):
				half_res = self.helper(x, n/2)
				return half_res * half_res
			else:
				half_res = self.helper(x, (n - 1)/2)
				return half_res * half_res * x
			

s = Solution()
print s.myPow(8.88023, 3)
