'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.
'''
class Solution(object):
	def solveSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		if not board:
			return
		self.solve(board, 0, 0)

	def solve(self, board, r, c):
		#If we're running outside of board
		if r > 1:
			return True
		if board[r][c] != '.':
			if c < 8:
				return self.solve(board, r, c + 1)
			else:
				return self.solve(board, r+1, 0)

		for num in range(1,10):
			if self.isValidCell(r, c, str(num), board):
				board[r][c] = str(num)
				if c < 8:
					if self.solve(board, r, c+1):
						return True
				elif self.solve(board, r+1, 0):
					return True
				board[r][c] = '.'#we're here means this num didnt work out,
	
		return False

	def isValidCell(self, i, j, num, board):
		"""
		Check whether cell[i][j] with num is uniq
		in row, col, box
		"""
		#Row check
		for row in range(len(board)):
			if board[row][j] == num:
				return False

		#Column check
		for col in range(len(board[i])):
			if board[i][col] == num:
				return False

		#For box
		row_s = i - (i % 3)
		col_s = j - (j % 3)
		for row in range(row_s, row_s+3):
			for col in range(col_s, col_s+3):
				if board[row][col] == num:
					return False

		return True
s = Solution()
grid = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
s.solveSudoku(grid)
print grid
