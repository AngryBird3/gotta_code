class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        if len(nums) == 0:
            return None
        '''
        if len(nums) == 1:
            if k <= 1:
                return nums[0]
            else:
                return None
        if k >= len(nums):
            return None
        '''
        l = 0 
        r = len(nums) - 1 
        while(True):
            pos = self.partition(nums, l, r)
            if (pos == k-1): 
                return nums[pos]
            elif pos >= k:
                r = pos - 1 
            else:
                l = pos + 1 
        
    def partition(self, nums, l, r):
        x = nums[r]
        i = l 
        for j in range(l, r): # left to right -1
            if nums[j] > x:  # the larger elements are in left side
                self.swap(nums, i, j)
                i += 1
        self.swap(nums, i, r)# swap the i and the last element, 
							 #to keep pivot at its right position in sorted
        return i
            
    def swap(self, nums, a, b): 
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp

