'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
'''
class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
        opt = [0] * (len(num) + 2)
        opt[0] = num[0] 
        opt[-1] = 0 
        for i in range(1, len(num)):
            print opt[i-1]
            opt[i] = max(opt[i - 2] + num[i], opt[i - 1]) 
            print "opt[",i,"]: ", opt[i]
        return opt[len(num) - 1]
