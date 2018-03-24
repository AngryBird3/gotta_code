class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        min_dist = float('inf')
        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    dist = list()
                    self.bfs(grid, i, j, dist, 1, m, n)
                    min_dist = min(min_dist, sum(grid))
                    
        return min_dist
        
    def bfs(self, grid, i, j, dist, l, m, n):
        print "i: ", i, " j : ", j
        if grid[i][j] == 1:
            dist.append(l)
            return
        if i+1 < m and grid[i][j] < 1:
            self.bfs(grid, i+1, j, dist, l+1, m, n)
        if i-1 > -1 and grid[i][j] < 1:
            self.bfs(grid, i-1, j, dist, l+1, m, n)
        if j+1 < n and grid[i][j] < 1:
            self.bfs(grid, i, j+1, dist, l+1, m, n)
        if j-1 > -1 and grid[i][j] < 1:
            self.bfs(grid, i, j-1, dist, l+1, m, n)
        return

s = Solution()
print s.shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]])
