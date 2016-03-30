'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
https://leetcode.com/discuss/42700/explain-like-im-five-java-solution-in-o-n
'''
from math import factorial
class Solution(object):
	def getPermutation(self, n, k):
		"""
		:type n: int
		:type k: int
		:rtype: str
		"""
		if k > factorial(n):
			return ""
		nums = range(1, n+1)
		result = ""
		k -= 1
		for i in range(1, n+1):
			index = k/factorial(n - i)
			#print "index: ", index, " k: ", k, " i: ", i, " nums: ", nums
			result += str(nums[index])
			nums.pop(index)
			k = k - (index * factorial(n-i))

		return result

s = Solution()
print s.getPermutation(2, 11)
