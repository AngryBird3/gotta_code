'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Hide Tags Array Dynamic Programming
Difficulty: Medium
'''
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        opt = [None] * len(triangle) 
        opt[0] = [triangle[0][0], 0]

        for i in range(1, len(triangle)):
            opt[i] = [float('inf')] * len(triangle[i])
            for j in range(0, len(triangle[i])):
                if j < (len(triangle[i-1])):
                    opt[i][j] = opt[i-1][j] + triangle[i][j]
                if j > 0:
                    opt[i][j] = min(opt[i][j], \
                                    opt[i-1][j-1] + triangle[i][j])
            #print opt[i]

        return min(opt[-1])

'''
New idea:
I can go from bottom to top
ans : [0]

for layer in range(n-2, -1, -1):
	opt[i] = min(opt[i], opt[i+1]) + triangle[layer][i]
return opt[0]
'''
'''
