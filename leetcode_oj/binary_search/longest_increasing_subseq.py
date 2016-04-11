'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

Hide Company Tags Microsoft
Hide Tags Dynamic Programming Binary Search
Show Similar Problems
'''
import bisect
class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		'''
		Algorithm:
		- Keep longest increasing sub sequence array - opt
		- if i > opt[-1]: append
		- else Find index where current should fit it
			- insert then and remove remaining
		- why?
		- To make sure we ALWAYS have minimum in opt
		'''
		if not nums:
			return 0

		opt = [float('inf')] * len(nums)
		opt[0] = nums[0]
		l = 1
		print opt[:l+1]
		for i in range(1, len(nums)):
			if nums[i] > opt[l-1]:
				opt[l] = nums[i]
				l += 1
			else:
				index = bisect.bisect_left(opt, nums[i])
				print index
				opt[index] = nums[i]
				#l = index+1
			print opt[:l+1]
		return l
s = Solution()
print s.lengthOfLIS([1,3,6,7,9,4,10,5,6])
