'''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

Show Tags
Show Similar Problems
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        f = self.first(nums, target)
        if f == -1:
            return [-1, -1]
        l = self.last(nums, target, f)
        
        return [f, l]
        
    def first(self, nums, target):
        """
        return first index of target
        """
        start = 0; end = len(nums) - 1
        while (start < end):
            mid = start + (end - start)/2
            if target > nums[mid]:
                start = mid + 1
            else:
                end = mid
        if nums[start] == target:
            return start
        return -1
                
    def last(self, nums, target, start):
        """
        return last index of target
        """
        end = len(nums) - 1
        while start < end:
            mid = (start + end) /2 + 1;   # Make mid biased to the right
            if target < nums[mid]:
                end = mid - 1
            else:
                start = mid
        if nums[start] == target:
            return start
        return -1
                
s = Solution()
print s.searchRange([1,2, 2, 2, 3],0)
