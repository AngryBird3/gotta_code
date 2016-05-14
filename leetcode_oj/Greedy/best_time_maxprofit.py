'''
122. Best Time to Buy and Sell Stock II   My Submissions QuestionEditorial Solution
Total Accepted: 86868 Total Submissions: 204670 Difficulty: Medium
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Hide Company Tags Bloomberg
Hide Tags Array Greedy
Hide Similar Problems (E) Best Time to Buy and Sell Stock (H) Best Time to Buy and Sell Stock III (H) Best Time to Buy and Sell Stock IV (M) Best Time to Buy and Sell Stock with Cooldown
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0 

        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profit += (prices[i+1] - prices[i]) 

        return profit
