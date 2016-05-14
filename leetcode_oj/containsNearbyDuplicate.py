'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

Hide Company Tags Palantir Airbnb
Hide Tags Array Hash Table
Hide Similar Problems (E) Contains Duplicate (M) Contains Duplicate III
Difficulty: Easy
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        d = {} #key: elem, val: index in nums
        for i in range(len(nums)):
            if nums[i] in d and (i - d[nums[i]]) <= k:
                return True
            else:
                d[nums[i]] = i
        return False
