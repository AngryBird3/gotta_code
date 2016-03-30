'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a <= b <= c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
	def threesum(self, nums):
		h = {}
		for i in range(len(nums)):
			h[nums[i]] = i
	
		res = list()
		for i in range(len(nums)):
			a = nums[i]
			for j in range(i+1, len(nums)):
				b = nums[j]
				c = 0 - nums[i] - nums[j]
				if c in h and h[c] > j:
					res.append([a, b, c])
		return res

	def threesum2(self, nums):
		nums.sort()
		h = {}
		for i in range(len(nums)):
			h[nums[i]] = i
	
		res = list()
		for i in range(len(nums)):
			if i == 0 or nums[i] != nums[i-1]:
				a = nums[i]
				for j in range(i+1, len(nums)):
					if j==i+1 or nums[j] != nums[j-1]:
						b = nums[j]
						c = 0 - nums[i] - nums[j]
						if c in h and h[c] > j:
							res.append([a, b, c])
		return res

s = Solution()
#print s.threesum2([-1,0,1,2,-1,-4])
print s.threesum2([0,0,0,0])
