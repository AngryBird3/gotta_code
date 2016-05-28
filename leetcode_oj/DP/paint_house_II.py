class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0
            
        n = len(costs)
        k = len(costs[0])
        
        min1_k = -1  #Storing minimum cost (some 0..k) till now
        min2_k = -1  #Storing second minimum cost (some 0...k index) till now
        last_min2_k = -1
        last_min1_k = -1
        for i in range(n):
            min1_k = last_min1_k
            min2_k = last_min2_k
            
            last_min1_k = -1
            last_min2_k = -1
            for j in range(k):
                # till now, all i house cost for jth color is
                # total_cost[i][j] = cost[i-1][min1_k] + cost[i][j]
                # i.e. minimum cost till previous (i-1), will use
                # minimum cost color, which is min1_k. 
                # Find new minimum once we try all j.
                if j != min1_k: #Can't color two adjacent house with same color
                    costs[i][j] +=  0 if min1_k < 0 else costs[i-1][min1_k]
                else:
                    costs[i][j] +=  0 if min2_k < 0 else costs[i-1][min2_k]
            
            
                #Update last_min1_k and last_min2_k for next house
                if last_min1_k < 0 or costs[i][j] < costs[i][last_min1_k]:
                    last_min2_k = last_min1_k ###THIS IS MUST: why? Cause otherwiise we'll have 3rd minimum or so, as 2nd min
                    last_min1_k = j
                elif last_min2_k < 0 or costs[i][j] < costs[i][last_min2_k]:
                    last_min2_k = j
                    
        return costs[n-1][last_min1_k]
                
                
