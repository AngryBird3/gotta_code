'''
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Hide Company Tags Bloomberg
Hide Tags Binary Search Array Two Pointers
Hide Similar Problems (H) First Missing Positive (M) Single Number (M) Linked List Cycle II (M) Missing Number
Difficulty: Hard
'''
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ''' 
        Algorithm:
        Pigenhole principal

        If there are n places, and n+1 elemnts -> 1 Elem has to repeat

        How to find that one?
        Binary search:  
        Count # of elements which are < the mid.
        

        Let count be the number of elements in the range 1 .. mid,

        If count > mid, then there are more than mid elements in the 
        range 1 .. mid and thus that range contains a duplicate.

        If count <= mid, then there are n+1-count elements in the range 
        mid+1 .. n. That is, at least n+1-mid elements in a range of size 
        n-mid. Thus this range must contain a duplicate.

        Or less formally:

        We know that the whole range is "too crowded" and thus that the 
        first half or the second half of the range is too crowded (if both 
        weren't, then neither would be the whole range). So you check to 
        know whether the first half is too crowded, and if it isn't, you know 
        that the second half is.
        '''

        s = 0; e = len(nums) - 1 
        while s <= e:
            mid = (s+e)/2
            count = sum(i <= mid for i in nums)
            if count > mid:
                e = mid - 1 
            else:
                s = mid + 1 
        return s
