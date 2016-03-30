'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

Note:
The solution is guaranteed to be unique.
'''
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
		"""
		:type gas: List[int]
		:type cost: List[int]
		:rtype: int
		"""
		# To travel from i to i+1: (tank=) gas[i] - cost[i] is require
		# if its 0, we cant reach from i to i+1, restart looking for
		# start to i+1.
		# If total is greater than 0, I mean gas is more than cost
		# difinately solution exists
		total = 0; tank = 0; start = 0	
		for i in range(len(gas)):
			tank += gas[i] - cost[i]
			total += tank
			if tank < 0:
				tank = 0
				start = i + 1		

		if total < 0:
			return -1
		else:
			return start

s = Solution()
print s.canCompleteCircuit([10, 20, 20], [20, 10, 10])
