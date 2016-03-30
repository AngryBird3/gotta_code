'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1
https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order
''' 
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
		#1) Find largest index k for which nums[k] < nums[k+1]
        k = -1
        for i in range(len(nums) - 2, -1, -1):
                if nums[i] < nums[i+1]:
                        k = i 
                        break
        if k == -1: 
                return nums.reverse()
        #2) Find the largest index l for which nums[k] < nums[l]
        l = None
        for i in range(len(nums)-1, -1, -1):
                if nums[k] < nums[i]:
                        l = i 
                        break
        #3) Swap k and l
        nums[k], nums[l] = nums[l], nums[k]
            
        #4) Reverse index from k+1 to n
        start = k+1 
        end = len(nums)-1
        while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

s = Solution()
a = [1,2,3]
s.nextPermutation(a)
print a
