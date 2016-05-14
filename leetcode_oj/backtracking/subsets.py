class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = list()
        nums.sort()
        self.helper(nums, 0)
        return self.res
        
    def helper(self, nums, start, temp=list()):
        #if temp not in res:
        self.res.append(temp[:])
        
        for i in range(start, len(nums)):
            if i != start and nums[i] == nums[i-1]:
                continue
            temp.append(nums[i])
            self.helper(nums, i+1, temp)
            temp.pop()
            
