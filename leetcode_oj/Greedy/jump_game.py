'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
'''
class Solution(object):
    def canJump(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums) <= 1:
			return True
		jump = nums[0]
		for i in range(1, len(nums)):
			if jump == 0:
				return False
			jump -= 1
			jump = max(jump, nums[i]) 

		return True
				

s = Solution()
print s.canJump([5,9,3,2,1,0,2,3,3,1,0,0])
