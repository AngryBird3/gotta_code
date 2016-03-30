'''
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''
import collections
class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
	def solve(self, board):
		if not board:
			return
		
		row, col = len(board), len(board[0])
		q = collections.deque()
		
		for i in xrange(row):
			if board[i][0] == "O":
				q.append((i, 0))
			if board[i][col - 1] == "O":
				q.append((i, col -1))
	
		for j in xrange(col):
			if board[0][j] == "O":
				q.append((0, j))
			if board[row-1][j] == "O":
				q.append((row-1, j))

		while q:
			r, c = q.popleft()
			l = list(board[r])
			l[c] = 'B'
			board[r] = "".join(l)
			
			if r > 0 and board[r-1][c] == "O":
				q.append((r-1,c))
			if r < row - 1 and board[r+1][c] == "O":
				q.append((r+1, c))
			if c > 0 and board[r][c-1] == "O":
				q.append((r,c-1))
			if c < col - 1 and board[r][c+1] == "O":
				q.append((r,c+1))

		#Recover
		for i in xrange(row):
			for j in xrange(col):
				if board[i][j] == "X":
					continue
				l = list(board[i])
				l[j] = "O" if l[j] == "B" else "X"
				board[i] = ''.join(l)

s = Solution()
#board = ["OOOO", "OOOO", "OOOO"]
#board = ["XXXX", "XOOX", "XXOX", "XOXX"]
board = ["OXXOX", "XOOXO", "XOXOX", "OXOOO", "XXOXO"]
s.solve(board)
for i in range(len(board)):
	print ""
	for j in range(len(board[i])):
		print board[i][j], " ",

