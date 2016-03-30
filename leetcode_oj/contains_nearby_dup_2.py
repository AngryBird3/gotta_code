'''
Contains Duplicate 
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		h = {}
		a = list()
		for i in range(0, len(nums)):
			if nums[i] in h:
				h[nums[i]].append(i)
				a.append(nums[i])
				h[nums[i]].sort()
			else:
				h[nums[i]] = [i]

		for n in a:
			for i in range(0, len(h[n]) - 1):
				diff = h[n][i+1] - h[n][i]
				if diff <= k:
					return True
		return False

s = Solution()
a = [8, 9, 4, 13, 17, 4]
print s.containsNearbyDuplicate(a, 3)
