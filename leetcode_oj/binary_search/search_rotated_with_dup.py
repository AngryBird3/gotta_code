'''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
'''
class Solution(object):
    def search(self, nums, target):
        """
            :type nums: List[int]
             :type target: int
             :rtype: bool
             """
             l = 0
             r = len(nums) - 1

             while l <= r:
                print "l: ", l, " r: ", r
                m = (l+r)/2

             if nums[m] == target:
                return True

             while l < m and nums[l] == nums[m]:
                l += 1

            #First half sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
            #Second half sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            return False
