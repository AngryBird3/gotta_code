'''
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Hide Tags Greedy
Difficulty: Hard
'''
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [0] * len(ratings)
        candies[0] = 1
        
        #Front ...
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
            else:
                candies[i] = 1
        
        #Back ...
        total = candies[len(ratings)-1]
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                candies[i] = candies[i+1] + 1
            total += candies[i]
    
        return total
