'''
Given an array of integers, determine whether or not there exist two elements in the array (at different positions) whose sum is equal to some target value. Examples: [5, 4, 2, 4], 8 --> true [5, 1, 2, 4], 8 --> false 
'''
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {bool}
    def two_sum(self, nums, target):
        h = {}
        for i in range(len(nums)):
            other = target - nums[i]
            if other in h:
                return True
            if nums[i] not in h:
                h[nums[i]] = True
        return False

s = Solution()
#Test1 : Edge case - Empty
print s.two_sum([], 0) #False
#Test2: Different position
print s.two_sum([5], 10) #False
#Test3: Two Different positions
print s.two_sum([5], 5) #False
#Test4: Given
print s.two_sum([5, 4, 2, 4], 8) #True
#Test5: Givem
print s.two_sum([5, 1, 2, 4], 8) #False
#Test6: 
print s.two_sum([5,5], 10) #True
