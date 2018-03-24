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
            print "start: ", start, " nums[i]: ", nums[i], " temp: ", temp, " i: ", i
            self.helper(nums, i+1, temp)
            print "start: ", start, "poping ...: ", temp[-1], " temp: ", temp, " i: ", i
            temp.pop()
            
s = Solution()
nums = ['a','b','c']
res = s.subsetsWithDup(nums)
print "res: ", res
