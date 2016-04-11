'''
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note: 
Each combination's factors must be sorted ascending, for example: The factors of 2 and 6 is [2, 6], not [6, 2].
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples: 
input: 1
output: 
[]
input: 37
output: 
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
'''
class Solution(object):
	def getFactors(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		if n <= 1:
			return list()
		res = list()
		for i in range(2, n/2+1):
			if n % i == 0 and n/i >= i:
				res.append([i, n/i])
				more_res = self.getFactors(n/i)
				#Only append if the first number is > i (as results
				#are in ascending order, we don't wanna repeat either)
				for r in more_res:
					if r[0] >= i:
						res.append([i] + r)
		return res
					
s = Solution()
print s.getFactors(32)
