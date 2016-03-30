'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
'''
class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		self.res = list()
		nums.sort()
		self.helper(nums)
		return self.res

	def helper(self, nums, temp=list()):
		if not nums:
			print temp
			self.res.append(temp[:])
		for i in range(len(nums)):
			#print " i: ", i, " temp: ", temp, " nums: ", nums
			temp.append(nums[i])
			if i < 1 or nums[i] != nums[i-1]:
				self.helper(nums[:i]+nums[i+1:], temp)
			temp.pop()
s = Solution()
print s.permuteUnique([1, 1, 2])
