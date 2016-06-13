'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

Notes:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
Credits:
Special thanks to @stellari for adding this problem and creating all test cases.

Hide Company Tags Microsoft
Hide Tags Binary Search Dynamic Programming
Hide Similar Problems (M) Unique Paths (M) Minimum Path Sum
Difficulty: Hard

Notes:
-2   -3   3
-5   -10  1
10    30  -5


Think like power vs sweat .
We need to calculate positive power at right most last corner to reach to Princess

We'll start from there, To calculate how much power I need at there.

Then I can go ONLY up or left (As Knight can move right or down)

So from last. Start filling.

?,?,?
?,?,?
?,?,6

For last row: we can only move FROM right.
So opt[i][j] = Minimum HP(power) needed to reach from [i][j] to [m][n]

Ok. So last row.
sweat = dungeon
opt[m][j] = max(opt[i][j+1] - sweat[i][j], 1)
max cause say 6 - 30. Is minimum, but power has to be positive -- at least 1


For Last column, same thing. Only come from down.
opt[i][n] = max(opt[i-1][n] - sweat[i][j], 1)

?,?,2
?,?,5
1,1,6

For others its minimum of those two :
min(right, down)

7,5,2
6,11,5
1,1,6
'''
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        opt = [[0 for j in range(n)] for i in range(m)]
        #print "m: ", m, " n: ", n
        opt[m-1][n-1] = max(1 - dungeon[m-1][n-1], 1)
        #print opt
        #Last row
        for j in range(n - 2, -1, -1):
            #required_power = at least 1
            # or power_had - sweat
            # like cost - gas!
            opt[m-1][j] = max(opt[m-1][j+1] - dungeon[m-1][j], 1)
        #print opt    
        #Last column
        for i in range(m - 2, -1, -1):
            opt[i][n-1] = max(opt[i+1][n-1] - dungeon[i][n-1], 1)
            
        #print opt
        #For other cells, fill in with min(up, right)
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
   
                right = max(opt[i][j+1] - dungeon[i][j], 1)
                down = max(opt[i+1][j] - dungeon[i][j], 1)
                opt[i][j] = min(right, down)
        #print opt       
        return opt[0][0]
