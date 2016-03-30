#!/usr/bin/python
'''
We maintain two amounts, the current one is: day i can reach up to j transaction, 
how much profit is the best (global [i] [j]),
The other: day i was currently reaches up to j times the transaction, 
and the number of the last trading day of the best profit in selling the (local [i] [j]).
Here we look at recursive globally is relatively simple,

global [i] [j] = max (local [i] [j], global [i-1] [j]),
That is the best to go to the current local and global best 
in the past that large (because the last trading day if 
it contains certain current local best inside,
Otherwise it must be in the past inside the global optimum).

Global (i days j reaches the maximum transaction gains) 
	= max {local (i after the first day of trading, just to meet the transaction j), 
			Global (j-1 reaches the first day of the transaction have been met j)}


For the maintenance of local variables, recursive formula is

local [i] [j] = max (global [i-1] [j-1] + max (diff, 0), local [i-1] [j] + diff),
'''
class Solution:
    # @return an integer as the maximum profit 
    def maxProfit(self, k, prices):
	if k < 2 or len(prices) == 0:
		return 0

	my_global = local = [[0 for x in range(k)] for x in range(len(prices))] 
	#my_global i max Profit across days, J Transactions
	#local Till i max Profit Day, J Transactions, Where there is transaction happening on i day	
	for i in range(1, len(prices)):
		print "------- --------", i, "-------- ---------"
		diff = prices[i] - prices[i-1]
		#print "---diff: ", diff
		for j in range(1, k):
			print "---",j,"---"
			print "local[i][j]: ", local[i][j]
			local[i][j] = max(my_global[i - 1][j - 1] + max(diff, 0), local[i-1][j] + diff)
			my_global[i][j] = max(my_global[i-1][j], local[i][j])
			#print "---local[i][j]: ", local[i][j]
			#print "---my_global[i][j]: ", my_global[i][j]
	return my_global[len(prices)-1][k-1]

s = Solution()
p = [100, 80, 85, 200]
k = 2
profit = s.maxProfit(k, p)
print "Prices: ", p, " k: ", k, " profit: ", profit
