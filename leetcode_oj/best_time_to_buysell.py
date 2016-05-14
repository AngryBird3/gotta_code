'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0 
        buy = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - buy)
            buy = min(buy, prices[i])
        return profit
