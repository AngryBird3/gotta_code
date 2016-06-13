'''
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

Hide Company Tags Microsoft
Hide Tags Array Binary Search
Hide Similar Problems (H) Search in Rotated Sorted Array (H) Find Minimum in Rotated Sorted Array II
Difficulty: Medium
'''
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        #Goal: find element for which left and right both index would be greater.
        return self.binary_find_min(nums, 0, len(nums) - 1)

    def binary_find_min(self, nums, start, end):
        if end < start:
            return nums[0]
        if start == end:
            return nums[start]
        mid = (start + end)/2
        if (mid <= start or nums[mid] < nums[mid - 1]) and (mid >= end or nums[mid] < nums[mid+1]):
            return nums[mid]
                
        #Decide whether we need to go to left half or right half
        if (nums[end] > nums[mid]):
            return self.binary_find_min(nums, start, mid - 1)
        else:
            return self.binary_find_min(nums, mid + 1, end)


