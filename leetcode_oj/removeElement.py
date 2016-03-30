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
