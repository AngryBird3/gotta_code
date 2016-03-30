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
		count = 0
		if grid == None or len(grid) == 0:
			return 0
		if isinstance(grid[0], list):
			for i in range(len(grid)):
				for j in range(len(grid[i])):
					if grid[i][j] == '1':
						count += 1
						self.merge(grid, i, j)
		return count

	def merge(self, grid, i, j):
		if i < 0 or j < 0 or i > (len(grid) - 1) or j > (len(grid[0]) - 1):
			return
		if grid[i][j] != '1':
			return
		grid[i][j] = '2'
		self.merge(grid, i - 1, j)
		self.merge(grid, i + 1, j)
		self.merge(grid, i, j - 1)
		self.merge(grid, i, j + 1) 		
		
s = Solution()
'''
grid = [['1','1','1','1','0'],
		['1','1','0','1','0'],
		['1','1','0','0','0'],
		['0','0','0','0','0']]
'''
grid = [['1', '0', '0', '0', '0'],
		['0', '1', '0', '0', '0'],
		['0', '0', '1', '0', '0'],
		['0', '0', '0', '1', '1']]

'''
grid = [1, 1, 0, 1, 0, 1, 1]
grid = [['1', '1', '1'],
		['0', '1', '0'],
		['1', '1', '1']]
'''
print s.numIslands(grid)

