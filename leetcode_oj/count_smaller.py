class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        """
        Algorithm:
        Merge sort/Counting inversion: if left # jumps to right (or vice versa)
        Sort and then see how each number moved, for example 5 moved 
        two spots to the right so there were two smaller numbers on its right
        """
        self.smaller = [0] * len(nums)
        self.merge_sort(list(enumerate(nums)))
        return self.smaller

    def merge_sort(self, nums):
        half = len(nums)/2
        if half:
            l, r = self.merge_sort(nums[:half]),\
                    self.merge_sort(nums[half:])
            m = len(l); n = len(r)
            i = 0; j = 0
            while i < m or j < n:
                print "i: ", i, " j: ", j
                if j == n or i < m and l[i][1] <= r[j][1]:
                    print "l: ", l[i], 
                    print " r: ", r[j] if j < n else None
                    self.smaller[l[i][0]] += j
                    nums[i+j] = l[i]
                    i += 1
                else:
                    nums[i+j] = r[j]
                    j += 1
        return nums

s = Solution()
smaller = s.countSmaller([2,5,1,3,4])

