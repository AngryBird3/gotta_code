'''
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

Show Company Tags
Hide Tags
'''
class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if not nums:
			return 0
		last_num = nums[0]; count = 1; index = 1
		for n in nums[1:]:
			if n == last_num:
				if count >= 2:
					count += 1
					continue
				else:
					nums[index] = n
					index += 1
					count += 1
			else:
				nums[index] = n	
				index += 1
				last_num = n
				count = 1
		return index

	def removeDuplicates2(self, nums):
		index = 0
		for i in range(len(nums)):
			if i < 2 or nums[i] > nums[index-2]:
				nums[index] = nums[i]
				index += 1
		return index

s = Solution()
nums = [1,1,1,2,2,3]
index = s.removeDuplicates2(nums)
print nums, index
