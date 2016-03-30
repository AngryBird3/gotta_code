'''
Contains Duplicate 
Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
	def containsNearbyDuplicate(self, nums, k):
		max_elem = k + 1
		h = {}
		l = list()
		# the difference between first and last element is at most k
		if len(nums) <= k:
			temp = {}
			for i in range(len(nums)):
				if nums[i] not in temp:
					temp[nums[i]] = 1	
			return len(temp) != len(nums)

		for i in range(max_elem):
			if nums[i] not in h:
				h[nums[i]] = 1
				l.append(nums[i])

		for i in range(max_elem, len(nums)):
			if len(h) != max_elem:
				return True
			del h[l[0]]
			del l[0]	
			if nums[i] not in h:
				h[nums[i]] = 1 
				l.append(nums[i])
		
		return len(h) != max_elem
s = Solution()
#a = [8, 9, 4, 13, 17, 4]
a = [2, 2]
print s.containsNearbyDuplicate(a, 1)
