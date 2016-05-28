'''
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

Hide Company Tags Facebook
Hide Tags Array Hash Table Stack Dynamic Programming
Hide Similar Problems (H) Largest Rectangle in Histogram (M) Maximal Square
Difficulty: Hard
'''
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        height_mat = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                height_mat[i][j] = height_mat[i-1][j] + 1 if matrix[i][j] == "1" else 0
        max_rect = 0
        for row in height_mat:
            max_rect = max(max_rect, self.largest_rectangle(row))
        
        return max_rect
        
    def largest_rectangle(self, height):
        height.append(0) #This is to empty stack in same loop, considering 424 cases
        stack = list()
        stack.append(-1) #our last height - 0
        max_area = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area
