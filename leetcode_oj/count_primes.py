'''
Description:

Count the number of prime numbers less than a non-negative number, n
'''
class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
		end = n
		c = 1
		nums = {}
		for j in range(2, end, 2):
			try:
				nums[j] = 1 
			except:
				pass
		
		for n in range(3, end):
			if n in nums:
				continue
			for i in range(2, n):
				if (n % i) == 0:
					break
			if i == (n-1):
				c += 1
				# Add multiple of n
				for j in range(n, end, n):
					try:
						nums[j] = 1 
					except:
						pass
		return c

s = Solution()
print s.countPrimes(1000)
