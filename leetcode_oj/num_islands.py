'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
'''

class Solution:
    # @param {character[][]} grid
    # @return {integer}
	def numIslands(self, grid):
		islnd_h = set()
		islnd_v = set()
		count = 0
		if len(grid) == 0:
			return 0
		if type(grid[0]) is not list:
			prev = None
			for i in range(len(grid)):
				if grid[i] == 1:
					if prev == None:
						count += 1
					elif prev == False:
						count += 1
					prev = True
				else:
					prev = False
			return count
					
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				print "i: ", i, "j: ", j, "val[i][j]: ", grid[i][j]
				if grid[i][j] == 1:
					print "islnd_h: ", islnd_h, "islnd_v: ", islnd_v
					if i not in islnd_h and j not in islnd_v:
						count += 1
					islnd_h.add(i)
					islnd_v.add(j)
					print "After adding islnd_h: ", islnd_h, "islnd_v: ", islnd_v
				else:
					print "islnd_h: ", islnd_h, "islnd_v: ", islnd_v
					if i in islnd_h:
						islnd_h.remove(i)
					if j in islnd_v:
						islnd_v.remove(j)
					print "After removing islnd_h: ", islnd_h, "islnd_v: ", islnd_v

		return count

s = Solution()
'''
grid = [[1,1,1,1,0],
		[1,1,0,1,0],
		[1,1,0,0,0],
		[0,0,0,0,0]]
grid = [[1, 0, 0, 0, 0],
		[0, 1, 0, 0, 0],
		[0, 0, 1, 0, 0],
		[0, 0, 0, 1, 1]]

grid = [1, 1, 0, 1, 0, 1, 1]
'''
grid = [[1, 1, 1],
		[0, 1, 0],
		[1, 1, 1]]
print s.numIslands(grid)
