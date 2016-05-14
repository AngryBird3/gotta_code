'''
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Hide Company Tags Palantir Airbnb Yahoo
Hide Tags Array Hash Table
Hide Similar Problems (E) Contains Duplicate II (M) Contains Duplicate III
'''
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        d = {}
        for n in nums:
            if n in d:
                    return True
            else:
                d[n] = 1
        return False
