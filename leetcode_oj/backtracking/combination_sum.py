'''
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
Hide Company Tags Snapchat Uber
Hide Tags Array Backtracking
Hide Similar Problems (M) Letter Combinations of a Phone Number (M) Combination Sum II (M) Combinations (M) Combination Sum III (M) Factor Combinations
Difficulty: Medium
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or not target:
            return list()
        self.res = list()
        candidates.sort()
        self.helper(candidates, target)
        return self.res

    def helper(self, nums, t, temp=list(), begin=0):
        if t < 0:
            return
        if not t:
            self.res.append(temp[:])
            return
                
        for i in range(begin, len(nums)):
            #if i < 1 or nums[i] != nums[i-1]:
            temp.append(nums[i])
            self.helper(nums, t-nums[i], temp, i)
            temp.pop()
