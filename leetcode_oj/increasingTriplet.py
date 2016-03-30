'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
'''
import numpy
class Solution(object):
	def increasingTriplet(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		'''
		Algorithm:
		At all time we need keep track of c1 (i) < c2 (j) < c3
	
		Update c1, c2, c3
		'''
		c1 = numpy.iinfo(numpy.int32).max 
		c2 = numpy.iinfo(numpy.int32).max

		for n in nums:
			if n <= c1: #Its less than min
				c1 = n
			elif n <= c2: #Its less that max
				c2 = n
			else:
				return True #This is greater than both c1 and c2
		return False
s = Solution()
print s.increasingTriplet([5, 5, 5, 5])
