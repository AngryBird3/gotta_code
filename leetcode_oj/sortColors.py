'''
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?
'''
class Solution(object):
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		'''
		Algorithm:
		1) with extra space we can do counting sort
		2) No space:
			- Move 2's to end and 0's to start 
		'''
		idx_zero =0
		idx_two = len(nums) - 1
		i = 0
		while i <= idx_two:
			#Move all ith "two" to end (idx_two)
			while i < idx_two and nums[i] == 2:
				nums[i], nums[idx_two] = nums[idx_two], nums[i]
				idx_two -= 1
			#Move all ith "zero" to begin (idx_zero)
			while i > idx_zero and nums[i] == 0:
				nums[i], nums[idx_zero] = nums[idx_zero], nums[i]
				idx_zero += 1 
			i += 1

s = Solution()
nums = [2, 0, 1, 2]
s.sortColors(nums)
print nums
