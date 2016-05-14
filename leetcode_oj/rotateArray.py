'''
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

[show hint]

Related problem: Reverse Words in a String II
'''
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        if (k < 0):
           return
        if (k > len(nums)):
           k = k % len(nums)
        if (k == 0): 
           return
        #Sol1: Rotate naive way 
        #Sol2: Split array n-k-1 is the point
        spt = len(nums) - k - 1 
        self.reverse(nums, 0, spt+1)
        self.reverse(nums, spt+1, len(nums))
        self.reverse(nums, 0, len(nums))

    def reverse(self, nums, start, end):
        i = start
        j = end - 1 
        while(i <= j): 
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i += 1
            j -= 1
            
s = Solution()
r = [1,2,3,4,5,6,7]
s.rotate(r, 3)
print r
