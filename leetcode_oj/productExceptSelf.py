'''
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)
'''
class Solution(object):
	def productExceptSelf(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[int]
		"""

		'''
		Algorithm:
		(Note this is how I solved first)
		res = [(1,1)]*n
		for i in range(1,n):
			res[i][0] = res[i-1][0] * num[i-1]
		for i in range(n-1-1, -1, -1):
			res[i][1] = res[i+1][1] * num[i+1]
		for i in range(n):
			output[i] = res[i][0] * res[i][1] 
		'''
		n = len(nums)
		if n <= 0: 
			return [1]
		res = [1] * n
		#Left
		for i in range(1, n):
			res[i] = res[i-1] * nums[i-1]
		
		#right
		right = 1
		for i in range(n-1-1, -1, -1):
			res[i] = res[i] * nums[i+1] * right
			right = right * nums[i+1]

		return res

s = Solution()
nums = [1, 5]
res = s.productExceptSelf(nums)
print res
