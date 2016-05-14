'''
Given an array and a value, remove all instances of that value in place and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given input array nums = [3,2,2,3], val = 3

Your function should return length = 2, with the first two elements of nums being 2.
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
		if len(nums) < 1:
			return
		new_index = 0
		for i in range(len(nums)):
			if nums[i] != val:
				nums[new_index] = nums[i]
				new_index += 1

		if new_index == 0:
			i = 0
			while nums:
				del nums[i]	
		return new_index+1

s = Solution()
a = [3]
print s.removeElement(a, 3)
print a
