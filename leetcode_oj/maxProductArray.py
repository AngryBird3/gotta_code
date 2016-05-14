'''
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Hide Company Tags LinkedIn
Hide Tags Array Dynamic Programming
Hide Similar Problems (M) Maximum Subarray (E) House Robber (M) Product of Array Except Self
Difficulty: Medium
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        minProduct = nums[0] # Even negative numbers make larger number
        maxProduct = nums[0]
        minTemp = minProduct
        maxTemp = maxProduct
        res = maxProduct
        for i in range(1, len(nums)):
            minProduct = min(nums[i] * maxTemp, minTemp * nums[i], nums[i])
            maxProduct = max(nums[i] * maxTemp, minTemp * nums[i], nums[i])
            minTemp = minProduct
            maxTemp = maxProduct
            #print "i : ", i, " minProduct: ", minProduct,  " maxProduct: ", maxProduct
            res = max(res, maxProduct)
        return res
