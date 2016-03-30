'''
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''
class Solution(object):
	def permute(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.res = list()
		self.helper(nums)
		return self.res

	def helper(self, nums, temp=list()):
		if not nums:
			self.res.append(temp[:])

		for i in range(len(nums)):
			temp.append(nums[i])
			self.helper(nums[:i]+nums[i+1:], temp)
			temp.pop()

s = Solution()
print s.permute([1,2,3])
