'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
	def singleNumber(self, nums):
		a = 0
		for x in nums:
			a = a ^ x

		return a

s = Solution()
print s.singleNumber([1, 4, 1, 6, 2, 4, 6])
