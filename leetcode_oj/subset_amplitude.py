'''
Given: array [6, 10, 6, 9, 7, 8]
Amplitude of a subsequence of array A is the difference between the largest and the smallest element
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
	def subsets(self, nums):
		self.res = list()
		self.helper(0, nums)

		return max(self.res)	

	def helper(self, start, nums, temp=list()):
		if temp:
			if max(temp) - min(temp) == 1:
				if len(temp) not in self.res:
					self.res.append(len(temp))

		for i in range(start, len(nums)):
			if temp:
				if abs(temp[0] - nums[i]) <= 1:
					temp.append(nums[i])
				self.helper(i+1, nums, temp)
			else:
				# If its empty just add that number
				temp.append(nums[i])
				self.helper(i+1, nums, temp)
			if temp:
				temp.pop() 

s = Solution()
print s.subsets([6, 10, 6, 9, 7, 8])
