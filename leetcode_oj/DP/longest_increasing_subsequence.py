'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''

class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		'''
		Algorithm:
		- If you sort it, you need to see indexes of sorted:
			opt[i] = opt[i-1] + 1 , if index[i] > index[i-1]
			result is in opt[n]
		- Ok , you dont need to sort it for that:
			opt[i] = Length of longest SUB sequence ending at i
			opt[i] = max(opt[j] + 1, opt[i]) where j is 0 .. i-1, nums[j] < nums[i];
			res = max(res, opt[i]) of course
		'''
		res = 0
		opt = [1] * len(nums)
		for i in range(len(nums)):
			for j in range(0, i):
				if nums[j] < nums[i]:
					opt[i] = max(opt[i], opt[j] + 1)
			res = max(res, opt[i])

		return res

s = Solution()
print s.lengthOfLIS([10, 10, 10])
