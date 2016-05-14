'''
33. Search in Rotated Sorted Array   My Submissions QuestionEditorial Solution
Total Accepted: 101224 Total Submissions: 333374 Difficulty: Hard
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Hide Company Tags LinkedIn Bloomberg Uber Facebook Microsoft
Hide Tags Binary Search Array
Hide Similar Problems (M) Search in Rotated Sorted Array II (M) Find Minimum in Rotated Sorted Array
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r)/2
            if nums[m] == target:
                return m
            #Search in lower part if its sorted:
            if nums[l] <= nums[m]:
                if nums[l] <= target and target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                #Upper part is sorted
                if nums[m] < nums[r]:
                    if nums[m] <= target and target <= nums[r]:
                        l = m + 1
                    else:
                        r = m - 1

        return -1
